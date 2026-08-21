-- Renders learning-outcome markers (Span/Link elements classed .ck/.pk/.pck/.l)
-- when building LaTeX/PDF output, matching handbook.css: an element also
-- classed .outcome becomes a pill-style, colored-background badge with black
-- text (program-outcome codes); otherwise (alignment-table cell markers) it
-- becomes a plain colored dot. HTML output is styled directly via CSS; this
-- filter is a no-op for non-LaTeX formats.
--
-- Keep the class -> LaTeX color name mapping in sync with GROUP_CLASSES in
-- tasks/table_generation.py and the badge/dot colors in handbook.css. The
-- \OutcomeBadge/\OutcomeDot commands and LaTeX color names are defined in
-- templates/outcome-colors.tex.

local LATEX_COLORS = {
  ck = "OutcomeCK",
  pk = "OutcomePK",
  pck = "OutcomePCK",
  l = "OutcomeL",
}

local function render(elem)
  if not FORMAT:match("latex") then
    return nil
  end
  for class, texcolor in pairs(LATEX_COLORS) do
    if elem.classes:includes(class) then
      if elem.classes:includes("outcome") then
        local text = pandoc.utils.stringify(elem.content)
        return pandoc.RawInline("latex", "\\OutcomeBadge{" .. texcolor .. "}{" .. text .. "}")
      end
      return pandoc.RawInline("latex", "\\OutcomeDot{" .. texcolor .. "}")
    end
  end
  return nil
end

return {
  { Span = render, Link = render },
}
