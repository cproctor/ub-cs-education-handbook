# UB Computer Science Education Handbook

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

## Building the handbook

To build the handbook run `pandoc` with the default settings:

    pandoc  -d defaults/handbook.yaml

To build other formats, specify an output file:

    pandoc  -d defaults/handbook.yaml -o ub_cs_handbook.0.0.2.pdf

See the [Pandoc manual](https://pandoc.org/MANUAL.html) for all the available
options.
