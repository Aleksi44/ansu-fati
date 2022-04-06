import argparse
from .serializers import LineSerializer


def execute_from_command_line(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args(argv)
    line_number = 0
    for line in args.file.readlines():
        line_modified = LineSerializer(line_number, line)
        print(f"{line_modified}")
        line_number += 1
