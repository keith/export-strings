import export_strings
import helpers
import os
import shutil
import unittest


class EnsureDirectoryTests(unittest.TestCase):
    def tearDown(self):
        shutil.rmtree(helpers.TEST_DIR)

    def test_ensuring_existing_directory(self):
        os.makedirs(helpers.SOURCE_DIR)
        export_strings.ensure_directory(helpers.SOURCE_DIR)
        self.assertTrue(os.path.isdir(helpers.SOURCE_DIR))

    def test_ensuring_nonexistant_directory(self):
        export_strings.ensure_directory(helpers.SOURCE_DIR)
        self.assertTrue(os.path.isdir(helpers.SOURCE_DIR))
