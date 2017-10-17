import os.path
import os


def init(debug=False, asan=False, ubsan=False):
    if not os.path.exists('build'):
        os.mkdir('build')
    os.chdir('build')
    cmake_flags = ''
    if debug:
        cmake_flags += ' -DCMAKE_BUILD_TYPE=Debug'
    else:
        cmake_flags += ' -DCMAKE_BUILD_TYPE=Release'
    if asan:
        cmake_flags += ' -DSANITIZE_ADDRESS=On'
    else:
        cmake_flags += ' -DSANITIZE_ADDRESS=Off'
    if ubsan:
        cmake_flags += ' -DSANITIZE_UNDEFINED=On'
    else:
        cmake_flags += ' -DSANITIZE_UNDEFINED=Off'
    os.system(f'cmake {cmake_flags} ..')


def make(task):
    os.chdir('build')
    os.system(f'make {task}')


def parse_args(argv):
    if argv[1] == 'init':
        init('--debug' in argv[2:], '--asan' in argv[2:], '--ubsan' in argv[2:])
    else:
        make(argv[1])


__all__ = ['parse_args']
