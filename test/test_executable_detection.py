import export_strings
import helpers
import os
import unittest


class ExecutableDetectionTests(unittest.TestCase):
    def test_checking_executable(self):
        self.assertTrue(export_strings.is_executable("/bin/bash"))

    def test_non_existant_path(self):
        self.assertFalse(export_strings.is_executable(helpers.FAKE_PATH))

    def test_non_executable_file(self):
        self.assertTrue(os.path.exists("README.md"))
        self.assertFalse(export_strings.is_executable("README.md"))
