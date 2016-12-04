from invalid_path_exception import InvalidPathException
import os


def ensure_directory(path):
    if not os.path.isdir(path):
        os.makedirs(path)


def is_executable(path):
    return (os.path.exists(path)
            and not os.path.islink(path)
            and os.access(path, os.X_OK))


def find_files(directory, is_match):
    root_directory = os.path.expanduser(directory)
    for root, _, files in os.walk(root_directory):
        for filename in files:
            full_path = os.path.join(root, filename)
            relative_path = os.path.relpath(full_path, root_directory)
            if is_match(full_path):
                yield relative_path, full_path


def find_executables(source, output):
    for relative_path, full_path in find_files(source, is_executable):
        output_path = os.path.join(output, relative_path)
        output_dir = os.path.dirname(output_path)
        ensure_directory(output_dir)
        yield full_path, output_path


def expand_and_validate(path):
    expanded_path = os.path.expanduser(path)
    if os.path.isdir(expanded_path):
        return expanded_path

    raise InvalidPathException(expanded_path)
