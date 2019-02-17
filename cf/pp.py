import contextlib
import os.path
import re
import sys


@contextlib.contextmanager
def open_write(filename):
    if filename != '-':
        with open(filename, 'w') as fout:
            yield fout
    else:
        yield sys.stdout


def run(args):
    include_pattern = r'#include "(.*)"'
    with open(args.input_file) as input_file, open_write(args.output_file) as output_file:
        for line in input_file:
            match = re.match(include_pattern, line)
            if match is not None:
                header_name = os.path.join(file_skeletons_dir, match[1])
                with open(header_name) as header_file:
                    line = header_file.read()
            output_file.write(line)


def parse_args(parser):
    parser.add_argument('input_file', metavar='INPUT-FILE')
    parser.add_argument('--output-file', '-o', metavar='OUTPUT-FILE', default='-')
    parser.set_defaults(run=run)


__all__ = ['parse_args']
