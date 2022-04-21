from unittest import TestCase
from tasks.writer import DataWriter
from more_itertools import peekable

SOURCE_SAMPLE = """

` @table:alignments:initial `{=comment}

| Learning outcome                           | LAI 552 | LAI 562 | LAI 574 | LAI 611 | LAI 663 | LAI 698 |
| ---------------------------------------    | ------- | ------- | ------- | ------- | ------- | ------- |
| PK1: Human development                     |         | X       | X       |         | X       |         |
| PK2: Learning                              |         |         | X       |         | X       |         |
| PK3: Supporting students with disabilities |         |         | X       | X       |         |         |
| PK4: Language acquisition and literacy     | X       | X       |         | X       |         |         |
| PK5: Curriculum and instruction            |         |         |         |         |         | X       |
| PK6: Professional practice and obligations |         |         |         |         |         | X       |
| PCK1: Computing as a literacy              | X       |         |         |         |         |         |
| PCK2: Supporting learner identities        | X       | X       |         |         | X       |         |
| PCK3: Shaping the learning environment     |         |         |         | X       |         |         |
| PCK4: Teaching with computational media    |         |         |         | X       |         |         |
| PCK5: Feedback and assessment              |         |         |         | X       |         |         |

"""

TINY_TABLE = "| Table |"
TABLE_WITH_BLANK = """

    | Table |
    | ----- |
    | Cell  |

"""
TABLE_WITH_TEXT_AFTER = """
| Table |
| ----- |
| Cell  |
What a table.
"""

class TestDataWriter(TestCase):

    def setUp(self):
        self.dw = DataWriter("source")

    def test_finds_marker(self):
        line = "` @table:alignments:initial `{=comment}"
        m = self.dw.read_marker(line)
        self.assertEqual(m[0], "@table")

    def test_iterate_past_table_returns_correct_number_of_lines(self):
        cases = (
            (TINY_TABLE, 1),
            (TABLE_WITH_BLANK, 5),
            (TABLE_WITH_TEXT_AFTER, 4),
        )
        for text, expected in cases:
            lines = text.split('\n')
            it = peekable(lines)
            observed = self.dw.iterate_past_table(it)
            self.assertEqual(len(observed), expected)

    def test_iterate_past_table_advances_iterator_correctly(self):
        cases = (
            (TINY_TABLE, 0),
            (TABLE_WITH_BLANK, 2),
            (TABLE_WITH_TEXT_AFTER, 2),
        )
        for text, expected in cases:
            lines = text.split('\n')
            it = peekable(lines)
            self.dw.iterate_past_table(it)
            observed = len(list(it))
            self.assertEqual(observed, expected)
