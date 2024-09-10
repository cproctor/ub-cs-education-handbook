from pathlib import Path
import re
from more_itertools import peekable
from tasks.table_generation import get_alignments
from datetime import datetime
import tomllib
import yaml

TRACKS = Path("data/tracks.yaml")
tracks = yaml.safe_load(TRACKS.read_text())

class DataWriter:
    """Updates representations of data in Markdown source. Allowed values:
        - @version
        - @table:alignments:<track>
        - @list:outcomes:<course>
    """
    markers = {
        "table": {"token": "@table", "regex": "@table:(\w+):(\w+)"},
        "list": {"token": "@list", "regex": "@list:(\w+):(\w+)"},
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
                        replacement_lines = self.generate_table_markdown(*marker)
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

    def generate_table_markdown(self, token, category, label):
        """Generates markdown for a table, iitialized with something like:
            @table:alignment:label
        """
        if token == "@table" and category == "alignment":
            if label not in tracks: 
                raise ValueError(f"Track {track} not recognized.")
            md = get_alignments(
                sorted(tracks[label]["courses"]), 
                tracks[label]["outcomes"],
                as_markdown=True
            )
            return [line + '\n' for line in [''] + md.split('\n')]
        raise ValueError(f"Could not generate {token}:{category}:{label}")

    def generate_list_markdown(self, token, category, label):
        """Generates markdown for a list, initialized with something like:
            @list:outcomes:676
        """
        if token == "@list" and category == "outcomes":
            alignments = get_alignments()
            if not label.isdigit() and int(label) in alignments.columns:
                raise ValueError(f"Invalid course number: {label}")
            outcomes = alignments.index[alignments[int(label)]]
            return '\n' + '\n'.join(f" - {o}" for o in outcomes)
        raise ValueError(f"Could not generate {token}:{category}:{label}")

    def generate_version_declaration(self):
        """Generates a version declaration, initialized with something like:
            @version
        """
        with open('pyproject.toml', 'rb') as fh:
            data = tomllib.load(fh)
        version = data['tool']['poetry']['version']
        timestamp = datetime.now().strftime("%B %-m, %Y")
        return f"\nVersion {version}. Generated on {timestamp}."
        
    def iterate_past_table(self, inlines):
        return self._iterate_past_whitespace_or_lines_starting_with(inlines, "|")

    def iterate_past_list(self, inlines):
        return self._iterate_past_whitespace_or_lines_starting_with(inlines, "-")

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

    def _iterate_past_whitespace_or_lines_starting_with(self, inlines, startchar):
        """Advances an iterator as long as lines are blank or their first non-whitespace character
        is startchar. Returns a list of discarded lines.
        See `iterate_past_table` and `iterate_past_list` for uses.
        """
        discard = []
        startchar_found = False
        while True:
            line = inlines.peek(None)
            if line is None:
                break
            sline = line.strip()
            if not ((sline == '' and not startchar_found) or sline.startswith(startchar)):
                break
            if sline.startswith(startchar):
                startchar_found = True
            discard.append(next(inlines))
        return discard
        
    def read_marker(self, line):
        "Returns a token, if one is found."
        for marker in self.markers.values():
            if marker["token"] in line:
                match = re.search(marker["regex"], line)
                if match:
                    return match.group(0).split(':')
