from pathlib import Path
import yaml
import pandas as pd

ALIGNMENTS = Path("data/alignments.yaml")
COURSES = Path("data/courses.csv")
OUTCOMES = Path("data/learning_outcomes.csv")

def get_alignments(courses=None, outcomes=None, as_markdown=False):
    course_df = pd.read_csv(COURSES, index_col="course_id")
    outcome_df = pd.read_csv(OUTCOMES, index_col="code")
    alignments = yaml.safe_load(ALIGNMENTS.read_text())
    df = pd.DataFrame(index=outcome_df.index, columns=course_df.index).fillna(False)
    for course, course_outcomes in alignments.items():
        for outcome in course_outcomes:
            df.loc[outcome, course] = True
    if courses:
        df = df[courses]
    if outcomes:
        df = df.loc[outcomes]
    if as_markdown:
        return df.replace(False, "").replace(True, "X").to_markdown()
    else:
        return df
