from pathlib import Path
import re
from more_itertools import peekable
from tasks.table_generation import get_alignments
import yaml

TRACKS = Path("data/tracks.yaml")
tracks = yaml.safe_load(TRACKS.read_text())

class DataWriter:
    """Updates representations of data in Markdown source. Allowed values:
        - @table:alignments:<track>
    """
    markers = {
        "table": {"token": "@table", "regex": "@table:(\w+):(\w+)"},
    }

    def __init__(self, sourcedir):
        self.sourcedir = Path(sourcedir)
        if not self.sourcedir.exists():
            raise ValueError(f"Path {self.sourcedir} does not exist.")

    def update_source_dir(self, sourcedir, dryrun=False):
        "Writes updates to source file for all markdown files in sourcedir."
        for filepath in Path(sourcedir).glob("**/*.md"):
            self.update_source_dir(fileapth, dryrun=dryrun)

    def update_source_file(self, filepath, dryrun=False, silent=False):
        "Writes updates to source file."
        with open(filepath) as fh:
            inlines = peekable(fh)
            outlines = []
            try: 
                while True:
                    line = next(inlines)
                    outlines.append(line)
                    marker = self.read_token(line)
                    if marker and marker[0] == self.marker["table"]["token"]:
                        discarded_lines = self.iterate_past_table(inlines)
                        replacement_lines = self.generate_table_markdown(*marker)
                        outlines += replacement_lines
                        if dryrun and not silent:
                            print(line)
                            print("OLD")
                            print(discarded_lines.join('\n'))
                            print("\nNEW")
                            print(replacement_lines.join('\n'))
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
            return get_alignments(
                tracks[label]["courses"], 
                tracks[label]["outcomes"],
                as_markdown=True
            )
        
    def iterate_past_table(self, inlines):
        discard = []
        table_found = False
        while True:
            line = inlines.peek(None)
            if line is None:
                break
            sline = line.strip()
            if not ((sline == '' and not table_found) or sline.startswith('|')):
                break
            if sline.startswith('|'):
                table_found = True
            discard.append(next(inlines))
        return discard
        
    def read_marker(self, line):
        "Returns a token, if one is found."
        for marker in self.markers.values():
            if marker["token"] in line:
                match = re.search(marker["regex"], line)
                if match:
                    return match.group(0).split(':')
