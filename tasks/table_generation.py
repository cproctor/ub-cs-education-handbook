import re
from pathlib import Path
import yaml
import pandas as pd

ALIGNMENTS = Path("data/alignments.yaml")
COURSES = Path("data/courses.csv")
OUTCOMES = Path("data/learning_outcomes.csv")

# Color-coding for learning outcome groups (CK/PK/PCK/L). These CSS class names
# must be kept in sync with the color definitions in handbook.css and the
# \definecolor commands in templates/outcome-colors.tex. The hex values
# themselves (#0ea5e9/#059669/#a855f7/#ea580c) were chosen so black badge text
# is readable on every color (all >=4.5:1 contrast) and all four stay
# distinguishable under simulated colorblindness in any pairing -- validated
# with the dataviz skill's scripts/validate_palette.js.
GROUP_CLASSES = {
    "CK": "ck",
    "PK": "pk",
    "PCK": "pck",
    "L": "l",
}

GROUP_NAMES = {
    "CK": "Content Knowledge",
    "PK": "Pedagogical Knowledge",
    "PCK": "Pedagogical Content Knowledge",
    "L": "Leadership",
}

# LaTeX \definecolor names for GROUP_CLASSES (see templates/outcome-colors.tex).
# Used when generating raw LaTeX directly (render_alignment_table_latex);
# elsewhere, filters/outcome-colors.lua maps GROUP_CLASSES to these same names.
GROUP_LATEX_COLORS = {
    "CK": "OutcomeCK",
    "PK": "OutcomePK",
    "PCK": "OutcomePCK",
    "L": "OutcomeL",
}


def outcome_group(code):
    "Returns the group prefix (CK, PK, PCK, or L) of an outcome code like 'PCK3'."
    match = re.match(r"[A-Za-z]+", code)
    if not match:
        raise ValueError(f"Could not determine group for outcome code {code!r}")
    return match.group(0)


def outcome_class(code):
    "Returns the CSS/LaTeX color class for an outcome code."
    return GROUP_CLASSES[outcome_group(code)]


def outcome_latex_color(code):
    "Returns the LaTeX \\definecolor name (see templates/outcome-colors.tex) for an outcome code."
    return GROUP_LATEX_COLORS[outcome_group(code)]


def load_outcome_names():
    return pd.read_csv(OUTCOMES, index_col="code")["name"].to_dict()


def outcome_badge(code, name=None, linked=True):
    """Renders an outcome code as a small colored, hyperlinked badge, e.g.
    '[CK1](#ck1 "Impacts of computing"){.outcome .ck}'. Does not declare the
    anchor -- the anchor id is declared once, where the outcome is defined,
    in source/vision_and_goals.md.
    """
    cls = outcome_class(code)
    title = f' "{name}"' if name else ""
    if linked:
        return f'[{code}](#{code.lower()}{title}){{.outcome .{cls}}}'
    return f'[{code}]{{.outcome .{cls}}}'


# Matches a "#### Fall Term 1 (6 credits)" / "#### Spring Term 2: Residency
# (9 credits)" style subheading in a track's "### Coursework" section.
TERM_HEADING_RE = re.compile(r'^####\s+(.+)$', re.MULTILINE)
COURSE_REF_RE = re.compile(r'\[LAI (\d+)\]')


def parse_semester_order(text, courses):
    """Orders `courses` by (semester taken, course code), using the Fall/Spring
    term subheadings (e.g. "#### Fall Term 1 (6 credits)") in a track file's
    "### Coursework" section to determine which semester each course is taken
    in.

    Returns (ordered_courses, dividers), where `dividers` is the list of
    positions (0-indexed into ordered_courses) after which a semester
    boundary falls, for drawing a divider between semester groups in the
    rendered alignment table.

    Returns None if the Coursework section has no term subheadings at all
    (an a-la-carte track with a single flexible-pace course list) -- callers
    should fall back to a plain sort in that case.
    """
    start = text.find("### Coursework")
    end = text.find("@table:alignment:", start if start >= 0 else 0)
    if start == -1 or end == -1:
        return None
    section = text[start:end]
    headings = list(TERM_HEADING_RE.finditer(section))
    if not headings:
        return None

    remaining = set(courses)
    ordered = []
    dividers = []
    for i, heading in enumerate(headings):
        block_start = heading.end()
        block_end = headings[i + 1].start() if i + 1 < len(headings) else len(section)
        block = section[block_start:block_end]
        found = {int(c) for c in COURSE_REF_RE.findall(block)}
        term_courses = sorted(found & remaining)
        if not term_courses:
            continue
        ordered.extend(term_courses)
        remaining -= set(term_courses)
        dividers.append(len(ordered) - 1)

    if remaining:
        # Courses not mentioned under any term heading (e.g. electives) --
        # append at the end, sorted, past a divider of their own.
        if ordered:
            dividers.append(len(ordered) - 1)
        ordered.extend(sorted(remaining))

    if dividers and dividers[-1] == len(ordered) - 1:
        dividers.pop()  # no divider after the very last column
    return ordered, dividers


def get_alignments(courses=None, outcomes=None, as_markdown=False, dividers=None):
    course_df = pd.read_csv(COURSES, index_col="course_id")
    outcome_df = pd.read_csv(OUTCOMES, index_col="code")
    alignments = yaml.safe_load(ALIGNMENTS.read_text())
    # Filled with a scalar (rather than the old NaN-then-fillna(False) dance)
    # so the frame is bool-dtype from the start -- pandas 2.x otherwise emits
    # a FutureWarning about the downcast fillna(False) used to perform.
    df = pd.DataFrame(False, index=outcome_df.index, columns=course_df.index)
    for course, course_outcomes in alignments.items():
        for outcome in course_outcomes:
            df.loc[outcome, course] = True
    if courses:
        df = df[courses]
    if outcomes:
        df = df.loc[outcomes]
    if as_markdown:
        return render_alignment_table(df, dividers=dividers)
    else:
        return df


def render_alignment_table(df, dividers=None):
    """Renders a compact, color-coded, hyperlinked alignment table as a pair
    of raw HTML/LaTeX blocks (Pandoc picks whichever matches the output
    format). Rows are outcomes (pill-style badges linking to their
    definitions); columns are courses (linking to course descriptions), in
    the order already set on df.columns; marked cells show a large colored
    dot in the outcome's group color.

    Raw blocks, rather than a portable Pandoc pipe table, are used here
    specifically so that `dividers` -- semester boundaries between courses,
    see parse_semester_order -- can be drawn as a real column rule (CSS
    border-left / a LaTeX "|" column spec) instead of a divider column
    holding literal "|" text, which would show up as stray characters in
    copied text or a screen reader.
    """
    html = render_alignment_table_html(df, dividers=dividers)
    latex = render_alignment_table_latex(df, dividers=dividers)
    return (
        "```{=html}\n" + html + "\n```\n"
        "```{=latex}\n" + latex + "\n```"
    )


def render_alignment_table_html(df, dividers=None):
    "Renders an alignment table (see render_alignment_table) as raw HTML."
    names = load_outcome_names()
    dividers = set(dividers or [])
    columns = list(df.columns)

    # The row-label ("Outcome") column always gets a divider, separating it
    # from the data columns, in addition to any semester dividers among them.
    header_cells = ['<th class="divider">Outcome</th>']
    for i, c in enumerate(columns):
        cls = ' class="divider"' if i in dividers else ""
        header_cells.append(f'<th{cls}><a href="#lai-{c}">{c}</a></th>')

    lines = ["<table>", "<thead><tr>" + "".join(header_cells) + "</tr></thead>", "<tbody>"]
    for code in df.index:
        cls = outcome_class(code)
        name = names.get(code, "")
        badge = f'<a href="#{code.lower()}" class="outcome {cls}" title="{name}">{code}</a>'
        cells = [f'<td class="divider">{badge}</td>']
        for i, c in enumerate(columns):
            td_cls = ' class="divider"' if i in dividers else ""
            dot = f'<span class="dot {cls}"></span>' if df.loc[code, c] else ""
            cells.append(f"<td{td_cls}>{dot}</td>")
        lines.append("<tr>" + "".join(cells) + "</tr>")
    lines += ["</tbody>", "</table>"]
    return "\n".join(lines)


def render_alignment_table_latex(df, dividers=None):
    "Renders an alignment table (see render_alignment_table) as raw LaTeX."
    dividers = set(dividers or [])
    columns = list(df.columns)

    # A "|" between column specs draws a real vertical rule at that boundary.
    # The row-label ("Outcome") column always gets one, separating it from
    # the data columns, in addition to any semester dividers among them.
    colspec = "l|" + "".join("c|" if i in dividers else "c" for i in range(len(columns)))

    header_cells = ["\\textbf{Outcome}"]
    header_cells += [f"\\textbf{{\\hyperlink{{lai-{c}}}{{{c}}}}}" for c in columns]

    lines = [
        f"\\begin{{longtable}}{{{colspec}}}",
        "\\toprule",
        " & ".join(header_cells) + " \\\\",
        "\\midrule",
        "\\endhead",
        "\\bottomrule",
        "\\endlastfoot",
    ]
    for code in df.index:
        texcolor = outcome_latex_color(code)
        cells = [f"\\OutcomeBadge{{{texcolor}}}{{{code}}}"]
        for c in columns:
            cells.append(f"\\OutcomeDot{{{texcolor}}}" if df.loc[code, c] else "")
        lines.append(" & ".join(cells) + " \\\\")
    lines.append("\\end{longtable}")
    return "\n".join(lines)


def get_track_outcomes_markdown(track, tracks):
    """Renders the color-coded, hyperlinked list of learning outcomes
    prioritized by a track, grouped in the order given in data/tracks.yaml,
    e.g. for the '### Learning outcomes' section of a track chapter.
    """
    if track not in tracks:
        raise ValueError(f"Track {track} not recognized.")
    names = load_outcome_names()
    lines = []
    for code in tracks[track]["outcomes"]:
        badge = outcome_badge(code, names.get(code))
        lines.append(f" - {badge}: {names.get(code, '')}")
    return "\n" + "\n".join(lines)
