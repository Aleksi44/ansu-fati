#!/usr/bin/env python
import sys

if __name__ == "__main__":
    from ansu_fati.command import execute_from_command_line
    execute_from_command_line(sys.argv[1:])
