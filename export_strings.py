#!/usr/bin/env python

from __future__ import print_function
from filesystem_helpers import *
from invalid_path_exception import InvalidPathException
import argparse
import os
import subprocess
import sys

SOURCE_HELP = "The source directory to walk and generate strings for"
OUTPUT_HELP = "The output directory for the strings files"
DEFAULT_COMMAND = ["strings"]


def validate_paths(source, output):
    source = expand_and_validate(source)

    if not output:
        output = os.path.basename(source)
        ensure_directory(output)

    output = expand_and_validate(output)
    return source, output


def process_executables(source, output, command):
    try:
        source, output = validate_paths(source, output)
    except InvalidPathException, exception:
        print(exception, file=sys.stderr)
        sys.exit(1)

    for full_path, output_path in find_executables(source, output):
        output = subprocess.check_output(command + [full_path])
        open(output_path, "w+").write(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", help=SOURCE_HELP, required=True)
    parser.add_argument("-o", "--output", help=OUTPUT_HELP)
    arguments = parser.parse_args()
    process_executables(arguments.source, arguments.output, DEFAULT_COMMAND)
