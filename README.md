# UB Computer Science Education Handbook

***Looking for the latest version of the handbook? Look in the "Releases" section of the right sidebar.***

This repository contains the source material for the CS education program handbook. 
The source documents are written in [Markdown](https://daringfireball.net/projects/markdown/) 
and built using [Pandoc](https://pandoc.org/MANUAL.html). 

There are several reasons for using this system (as opposed to just writing the handbook in Word):

- Track and store changes in version control
- Keep various parts of the handbook synchronized
- Handle tedious aspects of the build process, such as formatting citations, keeping the 
  references list up to date, and building the table of contents
- Export in multiple formats, including PDF, HTML, and docx.

## Installation

You will need the following packages installed. If using a mac, these can all be installed using homebrew.

- pandoc
- pandoc-crossref
- pandoc-plot
- A TeX Live distribution including `lualatex` (TeX Live 2023 or later; the
  PDF build depends on the LaTeX kernel's tagged-PDF support, which is still
  actively evolving, so staying reasonably current matters). The PDF is
  built as a tagged, PDF/UA-1 conformant document -- see the comments in
  `templates/eisvogel.latex` and `templates/outcome-colors.tex` for the
  accessibility-specific patches this depends on.
- [veraPDF](https://verapdf.org/) -- only needed to run the
  `verify-accessibility` task (see "Validating accessibility" below), not
  for a normal build. On a Mac, `brew install verapdf` (it's a Java tool, so
  this also pulls in a JDK); see its [install page](https://verapdf.org/software/)
  for other platforms.

## Building the handbook

To build the handbook run `pandoc` with the defaults file corresponding to the output format you want:

    pandoc  -d defaults/html.yaml
    pandoc  -d defaults/pdf.yaml

## Updating tables and lists

Program outcomes, and the courses in which they are taught and assessed, appear throughout the handbook. In order 
to keep them synchronized, a build task is avaiiable which updates tables and lists based on the data stored
in `data`. In order to use these tasks:

- Make sure [uv](https://docs.astral.sh/uv/) is installed.
- Run `uv sync`
- Enter `uv run inv --list` to see available tasks (e.g. `uv run inv update`).

See the [Pandoc manual](https://pandoc.org/MANUAL.html) for all the available
options.

## Validating accessibility

The PDF is built as a tagged document meeting the PDF/UA-1 standard (see
"Installation" above), which verifies that the document's structure is 
accessible. 

To check the built PDF against PDF/UA-1 (after installing veraPDF, and
building the PDF with `make pdf` or `pandoc -d defaults/pdf.yaml`):

    uv run inv verify-accessibility
