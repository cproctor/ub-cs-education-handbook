from pathlib import Path
import re
from more_itertools import peekable
from tasks.table_generation import get_alignments, get_track_outcomes_markdown, parse_semester_order
from datetime import datetime
import tomllib
import yaml

TRACKS = Path("data/tracks.yaml")
tracks = yaml.safe_load(TRACKS.read_text())

class DataWriter:
    """Updates representations of data in Markdown source. Allowed values:
        - @version
        - @table:alignment:<track>
        - @list:outcomes:<course>
        - @list:trackoutcomes:<track>
    """
    markers = {
        "table": {"token": "@table", "regex": r"@table:(\w+):(\w+)"},
        "list": {"token": "@list", "regex": r"@list:(\w+):(\w+)"},
        "version": {"token": "@version", "regex": "@version"},
    }

    def __init__(self, sourcedir):
        self.sourcedir = Path(sourcedir)
        if not self.sourcedir.exists():
            raise ValueError(f"Path {self.sourcedir} does not exist.")

    def update_source_dir(self, dryrun=False):
        "Writes updates to source file for all markdown files in sourcedir."
        for filepath in Path(self.sourcedir).glob("**/*.md"):
            self.update_source_file(filepath, dryrun=dryrun)

    def update_source_file(self, filepath, dryrun=False, silent=False):
        "Writes updates to source file."
        with open(filepath) as fh:
            inlines = peekable(fh)
            outlines = []
            try:
                while True:
                    line = next(inlines)
                    outlines.append(line)
                    marker = self.read_marker(line)
                    if marker and marker[0] == self.markers["table"]["token"]:
                        discarded_lines = self.iterate_past_table(inlines)
                        replacement_lines = self.generate_table_markdown(*marker, filepath=filepath)
                        outlines += replacement_lines
                        if dryrun and not silent:
                            print(line)
                            print("OLD")
                            print(''.join(discarded_lines))
                            print("\nNEW")
                            print(''.join(replacement_lines))
                    elif marker and marker[0] == self.markers["list"]["token"]:
                        discarded_lines = self.iterate_past_list(inlines)
                        replacement_lines = self.generate_list_markdown(*marker)
                        outlines += replacement_lines
                        if dryrun and not silent:
                            print(line)
                            print("OLD")
                            print(''.join(discarded_lines))
                            print("\nNEW")
                            print(''.join(replacement_lines))
                    elif marker and marker[0] == self.markers["version"]["token"]:
                        discarded_lines = self.iterate_past_version_declaration(inlines)
                        replacement_lines = self.generate_version_declaration()
                        outlines += replacement_lines
                        if dryrun and not silent:
                            print(line)
                            print("OLD")
                            print(''.join(discarded_lines))
                            print("\nNEW")
                            print(''.join(replacement_lines))
            except StopIteration:
                pass
        if not dryrun:
            with open(filepath, 'w') as fh:
                fh.writelines(outlines)

    # Tracks with no fixed term-by-term schedule -- coursework is taken "in
    # any order and pace" -- so their alignment table is just sorted by
    # course code, with no semester divider.
    A_LA_CARTE_TRACKS = {"professional", "advanced_certificate"}

    def generate_table_markdown(self, token, category, label, filepath=None):
        """Generates markdown for a table, iitialized with something like:
            @table:alignment:label
        """
        if token == "@table" and category == "alignment":
            if label not in tracks:
                raise ValueError(f"Track {label} not recognized.")
            courses = tracks[label]["courses"]
            order, dividers = None, []
            if label not in self.A_LA_CARTE_TRACKS and filepath:
                parsed = parse_semester_order(Path(filepath).read_text(), courses)
                if parsed:
                    order, dividers = parsed
            if order is None:
                order = sorted(courses)
            md = get_alignments(
                order,
                tracks[label]["outcomes"],
                as_markdown=True,
                dividers=dividers,
            )
            return [line + '\n' for line in [''] + md.split('\n')]
        raise ValueError(f"Could not generate {token}:{category}:{label}")

    def generate_list_markdown(self, token, category, label):
        """Generates markdown for a list, initialized with something like:
            @list:outcomes:676
            @list:trackoutcomes:initial
        """
        if token == "@list" and category == "outcomes":
            alignments = get_alignments()
            if not label.isdigit() and int(label) in alignments.columns:
                raise ValueError(f"Invalid course number: {label}")
            outcomes = alignments.index[alignments[int(label)]]
            from tasks.table_generation import outcome_badge, load_outcome_names
            names = load_outcome_names()
            badges = " ".join(outcome_badge(o, names.get(o)) for o in outcomes)
            return '\n' + badges + '\n\n'
        if token == "@list" and category == "trackoutcomes":
            return get_track_outcomes_markdown(label, tracks) + '\n\n'
        raise ValueError(f"Could not generate {token}:{category}:{label}")

    def generate_version_declaration(self):
        """Generates a version declaration, initialized with something like:
            @version
        """
        version = self.read_pyproject_version()
        timestamp = datetime.now().strftime("%B %-m, %Y")
        return f"\nVersion {version}. Generated on {timestamp}.\n"

    def read_pyproject_version(self):
        "Reads the canonical version number from pyproject.toml."
        with open('pyproject.toml', 'rb') as fh:
            data = tomllib.load(fh)
        return data['project']['version']

    def update_base_yaml_version(self, path="defaults/base.yaml", dryrun=False, silent=False):
        """Syncs defaults/base.yaml's metadata `version` field (and the version embedded
        in `date`) with the version declared in pyproject.toml, so the version only
        needs to be updated in one place.
        """
        version = self.read_pyproject_version()
        path = Path(path)
        text = path.read_text()

        new_text, n_version = re.subn(
            r'(?m)^(\s*version:\s*).*$', rf'\g<1>{version}', text, count=1
        )
        new_text, n_date = re.subn(
            r'(?m)^(\s*date:\s*.*?)\(Version [^)]*\)', rf'\g<1>(Version {version})',
            new_text, count=1
        )
        if n_version == 0 or n_date == 0:
            raise ValueError(f"Could not find version/date fields to update in {path}")

        if dryrun and not silent:
            print(f"{path}")
            print("OLD")
            print(text)
            print("\nNEW")
            print(new_text)
        if not dryrun:
            path.write_text(new_text)

    def iterate_past_table(self, inlines):
        """Advances past a previously-generated alignment table: either the
        legacy pipe-table ("|") or image-embed ("!") format, or the current
        pair of raw HTML/LaTeX fenced blocks (see
        table_generation.render_alignment_table) -- so that documents
        generated by earlier versions of this tool are migrated cleanly.
        Returns the discarded lines.
        """
        discard = []
        while True:
            line = inlines.peek(None)
            if line is None or line.strip() != '':
                break
            discard.append(next(inlines))
        first = inlines.peek(None)
        if first is None:
            return discard
        if first.strip().startswith(('|', '!')):
            discard += self._iterate_past_whitespace_or_lines_starting_with(inlines, ('|', '!'))
            return discard
        if first.strip().startswith('```'):
            # The fenced-block content itself (unlike a pipe table or list)
            # isn't line-prefixed, so it can't use
            # _iterate_past_whitespace_or_lines_starting_with -- instead,
            # discard through the second closing "```" fence (one each for
            # the html and latex blocks).
            closed = 0
            while closed < 2:
                line = inlines.peek(None)
                if line is None:
                    break
                discard.append(next(inlines))
                if line.strip() == '```':
                    closed += 1
        return discard

    def iterate_past_list(self, inlines):
        # Accepts both the legacy "- " bullet format and the current
        # hyperlinked-badge format (which starts with "[") so that documents
        # generated by earlier versions of this tool are migrated cleanly.
        return self._iterate_past_whitespace_or_lines_starting_with(inlines, ("-", "["))

    def iterate_past_version_declaration(self, inlines):
        """Advances through the first non-blank line.
        """
        discard = []
        while True:
            line = inlines.peek(None)
            if line is None:
                break
            discard.append(next(inlines))
            if line.strip():
                break
        return discard

    def _iterate_past_whitespace_or_lines_starting_with(self, inlines, startchars):
        """Advances an iterator as long as lines are blank or their first non-whitespace character
        matches one of startchars, then past a single trailing blank line if
        one follows. Returns a list of discarded lines.

        That trailing-blank-line step matters for idempotency: every
        generator in this module (see `generate_list_markdown`) ends its
        output with a blank-line separator, but the main loop below stops
        consuming blank lines as soon as it's seen the first startchars-line
        (so it doesn't run past the *start* of a following block) -- so
        without this extra step, that trailing blank line would never be
        recognized as part of the generated block, and `update` would leave
        one more blank line behind each time it's re-run.

        See `iterate_past_table` and `iterate_past_list` for uses.
        """
        if isinstance(startchars, str):
            startchars = (startchars,)
        discard = []
        startchar_found = False
        while True:
            line = inlines.peek(None)
            if line is None:
                break
            sline = line.strip()
            if not ((sline == '' and not startchar_found) or sline.startswith(startchars)):
                break
            if sline.startswith(startchars):
                startchar_found = True
            discard.append(next(inlines))
        if startchar_found:
            trailing = inlines.peek(None)
            if trailing is not None and trailing.strip() == '':
                discard.append(next(inlines))
        return discard

    def read_marker(self, line):
        "Returns a token, if one is found."
        for marker in self.markers.values():
            if marker["token"] in line:
                match = re.search(marker["regex"], line)
                if match:
                    return match.group(0).split(':')
