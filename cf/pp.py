import os.path
import re

def parse_args(argv):
    include_dir = '~/.config/codeforces/file-skeletons'
    include_dir = os.path.expanduser(include_dir)
    include_pattern = r'#include "(.*)"'
    with open(argv[1]) as input_file:
        for line in input_file:
            match = re.match(include_pattern, line)
            if match is not None:
                header_name = os.path.join(include_dir, match[1])
                with open(header_name) as header_file:
                    line = header_file.read()
            print(line, end='')

__all__ = ['parse_args']
