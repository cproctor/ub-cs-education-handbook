from pathlib import Path
from invoke import task, Exit
import yaml
import code
from tasks.table_generation import get_alignments

TRACKS = Path("data/tracks.yaml")

@task
def alignments_for_track(c, track, interact=False):
    import pandas as pd
    tracks = yaml.safe_load(TRACKS.read_text())
    if track not in tracks:
        raise ValueError(f"Track {track} not recognized.")
    df = get_alignments(tracks[track]["courses"], tracks[track]["outcomes"])
    print(df.replace(False, "").replace(True, "X").to_markdown())
    if interact:
        code.interact(local=locals())

@task
def update(c, dryrun=False):
    "Rewrite dynamic tables in source docs, and sync version from pyproject.toml"
    from tasks.writer import DataWriter
    writer = DataWriter("source")
    writer.update_source_dir(dryrun=dryrun)
    writer.update_base_yaml_version(dryrun=dryrun)

@task
def verify_accessibility(c, pdf=None, verbose=False):
    """Validates the built PDF against the PDF/UA-1 accessibility standard.

    PDF/UA-1 (ISO 14289-1) is the closest thing to an automatable proxy for
    WCAG 2.1 AA conformance in a PDF -- it's what confirms the document is
    genuinely tagged (real heading structure, alt text on figures, etc.),
    not just visually laid out. It doesn't cover everything WCAG 2.1 AA
    does (color contrast and the meaningfulness of alt text, for instance,
    still need a manual check), but it's the part that's actually
    machine-checkable.

    Requires veraPDF (https://verapdf.org/) to be installed and on PATH --
    see the "Validating accessibility" section of the README.
    """
    import shutil
    import tomllib
    if shutil.which("verapdf") is None:
        raise Exit(
            "veraPDF is not installed (or not on PATH). Install it from "
            "https://verapdf.org/ (e.g. `brew install verapdf` on a Mac), "
            "then try again."
        )
    if pdf is None:
        with open("pyproject.toml", "rb") as fh:
            version = tomllib.load(fh)["project"]["version"]
        pdf = f"ub_cs_education_handbook.{version}.pdf"
    pdf_path = Path(pdf)
    if not pdf_path.exists():
        raise Exit(f"{pdf_path} not found. Build it first with `make pdf`.")

    print(f"Validating {pdf_path} against PDF/UA-1 with veraPDF...")
    flags = "--format text" + (" -v" if verbose else "")
    c.run(f"verapdf {flags} {pdf_path}")

@task
def test(c):
    "Run all tests"
    import unittest
    test_suite = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(test_suite)

@task 
def serve(c, defaults_file):
    "Watch for changes and rebuild"
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    class PandocBuildEventHandler(FileSystemEventHandler):
        def on_modified(self, event):
            c.run(f"pandoc -d {defaults_file}")

    observer = Observer()
    handler = PandocBuildEventHandler()
    observer.schedule(handler, "source", recursive=True)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()


    

