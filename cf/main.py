#! /usr/bin/env python3

import sys

import cf.fetch
import cf.init

modules = {
    'fetch': cf.fetch,
    'init': cf.init,
}


def usage():
    pass


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in modules.keys():
        usage()
        sys.exit(1)
    modules[sys.argv[1]].parse_args(sys.argv[1:])


__all__ = ['main']
