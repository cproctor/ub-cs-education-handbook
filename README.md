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

## Building the handbook

To build the handbook run `pandoc` with the defaults file corresponding to the output format you want:

    pandoc  -d defaults/html.yaml
    pandoc  -d defaults/pdf.yaml

## Updating tables and lists

Program outcomes, and the courses in which they are taught and assessed, appear throughout the handbook. In order 
to keep them synchronized, a build task is avaiiable which updates tables and lists based on the data stored
in `data`. In order to use these tasks:

- Make sure [poetry](https://python-poetry.org/) is installed.
- Run `poetry install`
- Enter a `poetry shell`
- Enter `inv --list` to see available tasks.

See the [Pandoc manual](https://pandoc.org/MANUAL.html) for all the available
options.

## TODO

- Put the coursework into a schedule.
- Add fieldwork built into different courses.
- Show how 100 hours of fieldwork will be achieved prior to residency for initial teachers. 
