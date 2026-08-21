.PHONY: build pdf html update clean

# The version is canonically specified in pyproject.toml. `update` syncs it into
# defaults/base.yaml (and the source docs); this reads it for the output filenames.
VERSION := $(shell sed -n 's/^version = "\(.*\)"/\1/p' pyproject.toml)

# `make` with no target builds the handbook (pdf + html).
# Source docs are preprocessed first, to sync dynamic tables/lists with data/tracks.yaml
# and the version metadata with pyproject.toml.
build: update pdf html

pdf:
	pandoc -d defaults/pdf.yaml -o ub_cs_education_handbook.$(VERSION).pdf

html:
	pandoc -d defaults/html.yaml -o ub_cs_education_handbook.$(VERSION).html

# Rewrite dynamic tables/lists in source docs from data/tracks.yaml, and sync
# defaults/base.yaml's version metadata from pyproject.toml.
update:
	uv run inv update

clean:
	rm -f ub_cs_education_handbook*.pdf ub_cs_education_handbook*.html
	rm -rf export/*
	find . -name "__pycache__" -type d -exec rm -rf {} +
