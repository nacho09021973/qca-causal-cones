"""Regression tests for the Markdown-code false positive found during reconstruction."""

import unittest

from text_integrity import bare_display_lines, bad_chars, newline_suspects


class TextIntegrityTests(unittest.TestCase):
    def test_real_bare_math_is_reported(self):
        self.assertEqual(list(bare_display_lines("[\nx\n]")), [1, 3])

    def test_python_list_inside_fence_is_not_math(self):
        self.assertEqual(list(bare_display_lines("```python\na = [\n]\n```")), [])

    def test_math_after_fence_still_checked(self):
        self.assertEqual(list(bare_display_lines("~~~python\n]\n~~~\n[\nx\n]")), [4, 6])

    def test_short_or_different_fence_does_not_close(self):
        self.assertEqual(list(bare_display_lines("````python\n```\n~~~\n]\n````\n[")), [6])

    def test_controls_inside_code_still_reported(self):
        self.assertTrue(bad_chars("```\n\x08oxed\n```"))

    def test_lost_newline_inside_code_still_reported(self):
        self.assertTrue(newline_suspects("unused", "```\n\nabla x\n```"))


if __name__ == "__main__":
    unittest.main()
