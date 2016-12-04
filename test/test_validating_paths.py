import export_strings
import helpers
import invalid_path_exception
import os
import unittest

EXCEPTION = invalid_path_exception.InvalidPathException


class IntegrationTests(unittest.TestCase):
    def test_expand_existing(self):
        self.assertEqual(export_strings.expand_and_validate("~"),
                         os.path.expanduser("~"))

    def test_invalid_path(self):
        with self.assertRaises(EXCEPTION) as cm:
            export_strings.expand_and_validate(helpers.FAKE_PATH)
            self.assertIn(helpers.FAKE_PATH, cm.exception.__str__)

    def test_invalid_paths(self):
        with self.assertRaises(EXCEPTION) as cm:
            export_strings.validate_paths(helpers.FAKE_PATH, None)
            self.assertIn(helpers.FAKE_PATH, cm.exception.__str__)
