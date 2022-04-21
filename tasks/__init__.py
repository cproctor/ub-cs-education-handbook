from pathlib import Path
from invoke import task
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
def update(c):
    from tasks.writer import DataWriter
    writer = DataWriter("source")

@task
def test(c):
    "Run all tests"
    import unittest
    test_suite = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(test_suite)

    

