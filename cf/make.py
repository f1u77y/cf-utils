import os
import os.path
import subprocess


def init_run(args):
    if not os.path.exists('build'):
        os.mkdir('build')
    os.chdir('build')
    cmake_flags = []
    if args.debug:
        cmake_flags.append('-DCMAKE_BUILD_TYPE=Debug')
    else:
        cmake_flags.append('-DCMAKE_BUILD_TYPE=Release')
    if args.asan:
        cmake_flags.append('-DSANITIZE_ADDRESS=On')
    else:
        cmake_flags.append('-DSANITIZE_ADDRESS=Off')
    if args.ubsan:
        cmake_flags.append('-DSANITIZE_UNDEFINED=On')
    else:
        cmake_flags.append('-DSANITIZE_UNDEFINED=Off')
    subprocess.run(['cmake'] + cmake_flags + ['..'])


def make_run(args):
    if args.task == 'init':
        return init_run(args)
    os.chdir('build')
    os.system(f'make {args.task}')


def parse_args(parser):
    parser.add_argument('task')
    parser.set_defaults(run=make_run)
    parser.add_argument('--debug', action='store_false')
    parser.add_argument('--asan', action='store_false')
    parser.add_argument('--ubsan', action='store_false')


__all__ = ['parse_args']
