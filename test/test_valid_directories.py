import export_strings
import helpers
import os
import shutil
import unittest


class ValidDirectoryTests(unittest.TestCase):
    def setUp(self):
        os.makedirs(helpers.SOURCE_DIR)

    def tearDown(self):
        shutil.rmtree(helpers.TEST_APP)
        shutil.rmtree(helpers.TEST_DIR)

    def test_default_output_path(self):
        _, output = export_strings.validate_paths(helpers.SOURCE_DIR, None)
        self.assertEqual(output, helpers.TEST_APP)

    def test_valid_source_path(self):
        source, _ = export_strings.validate_paths(helpers.SOURCE_DIR, None)
        self.assertEqual(source, helpers.SOURCE_DIR)
