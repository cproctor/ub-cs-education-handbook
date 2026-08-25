-- Accessibility: pandoc's LaTeX writer has no built-in way to pass an
-- image's caption/alt text through to \includegraphics, so a Figure tag in
-- the tagged PDF ends up with no /Alt entry -- a PDF/UA-1 conformance
-- failure. This filter takes each image's caption (falling back to its
-- inline content, i.e. the Markdown "alt text" in `![alt](path)`) and sets
-- it as the `alt` key on the Image's attributes; the eisvogel template's
-- image handling (inherited from pandoc's default LaTeX writer) passes
-- attribute keys through to \includegraphics's optional argument, and the
-- LaTeX kernel's tagging-aware graphicx patches read `alt` from there.
--
-- No-op for non-LaTeX formats, where pandoc already emits alt text natively
-- (e.g. HTML's <img alt="...">).
local function image_alt(elem)
  if not FORMAT:match("latex") then
    return nil
  end
  local alt = pandoc.utils.stringify(elem.caption)
  if alt == "" then
    alt = pandoc.utils.stringify(elem.content)
  end
  if alt == "" then
    return nil
  end
  -- Escape braces so a caption containing them doesn't break the
  -- optional-argument key-value list.
  alt = alt:gsub("([{}])", "\\%1")
  elem.attributes["alt"] = alt
  return elem
end

return {
  { Image = image_alt },
}
