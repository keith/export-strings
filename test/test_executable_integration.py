import export_strings
import helpers
import os
import shutil
import unittest


class ExecutableFixtureTests(unittest.TestCase):
    def test_finding_specific_files(self):
        files = [x[0] for x in export_strings.find_files(helpers.FIXTURE_PATH, lambda _: True)]
        self.assertEqual(len(files), 4)
        self.assertIn("executable", files)
        self.assertIn("nested/nested_executable", files)
        self.assertIn("not_executable", files)
        self.assertIn("linked_executable", files)

    def test_full_path_exists(self):
        files = list(export_strings.find_files(helpers.FIXTURE_PATH,
                                               lambda _: True))
        path = files[0][1]
        self.assertTrue(os.path.exists(path))

    def test_relative_path_exists(self):
        files = list(export_strings.find_files(helpers.FIXTURE_PATH,
                                               lambda _: True))
        path = files[0][0]
        self.assertTrue(os.path.exists(
            os.path.join(helpers.FIXTURE_PATH, path)))

    def test_executable_output_paths(self):
        files = export_strings.find_executables(helpers.FIXTURE_PATH,
                                                helpers.TEST_DIR)
        for full_path, output_path in files:
            self.assertTrue(os.path.exists(full_path))
            self.assertEqual(output_path.split("/")[0], helpers.TEST_DIR)
            self.assertEqual(os.path.basename(full_path),
                             os.path.basename(output_path))
        shutil.rmtree(helpers.TEST_DIR)

    def test_executable_output_command(self):
        os.mkdir(helpers.TEST_DIR)
        export_strings.process_executables(helpers.FIXTURE_PATH,
                                           helpers.TEST_DIR, ["strings"])
        files = export_strings.find_executables(helpers.FIXTURE_PATH,
                                                helpers.TEST_DIR)
        for _, output_path in files:
            with open(output_path) as f:
                contents = f.read().strip()
            expected = "file: {}".format(os.path.basename(output_path))
            self.assertEqual(contents, expected)

        shutil.rmtree(helpers.TEST_DIR)

    def test_no_symlinks(self):
        os.mkdir(helpers.TEST_DIR)
        export_strings.process_executables(helpers.FIXTURE_PATH,
                                           helpers.TEST_DIR, ["strings"])
        files = export_strings.find_executables(helpers.FIXTURE_PATH,
                                                helpers.TEST_DIR)
        for original_path, _ in files:
            self.assertTrue(os.path.exists(original_path))
            self.assertFalse(os.path.islink(original_path))

        shutil.rmtree(helpers.TEST_DIR)
