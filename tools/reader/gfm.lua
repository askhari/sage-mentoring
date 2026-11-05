-- Pandoc filter for the Markdown reader (tools/build_reader.py, GFM output).
-- Keeps the text clean: no HTML wrappers, the document title as the first heading,
-- and a plain anchor before each heading so links like layer-2.md#c-hue keep working.

local title = nil

function Meta(meta)
  if meta.title then title = pandoc.utils.stringify(meta.title) end
end

-- Divs (reader-nav, references, key idea...) only exist for the HTML styles.
function Div(el)
  return el.content
end

-- "sin verificar" and other styled spans: keep the words, in italics.
function Span(el)
  if el.classes:includes("unverified") then
    return pandoc.Emph(el.content)
  end
  return el.content
end

-- The current-layer marker becomes bold text instead of an attribute.
function Link(el)
  if el.attributes["aria-current"] then
    return pandoc.Strong(el.content)
  end
  el.attr = pandoc.Attr()
  return el
end

-- Shift headings one level down (the title takes level 1). Concept (c-) and domain (d-) ids
-- are the link targets, so they stay as anchors; the rest are pandoc's own ids.
function Header(el)
  el.level = math.min(el.level + 1, 6)
  local id = el.identifier
  el.attr = pandoc.Attr()
  if id:match("^[cd]%-") then
    el.content:insert(1, pandoc.RawInline("html", '<a id="' .. id .. '"></a>'))
  end
  return el
end

return {{
  Pandoc = function(doc)
    doc = doc:walk({ Meta = Meta })
    doc = doc:walk({ Div = Div, Span = Span, Link = Link, Header = Header })
    if title then
      doc.blocks:insert(1, pandoc.Header(1, title))
    end
    return doc
  end,
}}
