#! /usr/bin/env python3

import sys

import cf.fetch
import cf.init
import cf.make
import cf.pp

modules = {
    'fetch': cf.fetch,
    'init': cf.init,
    'make': cf.make,
    'pp': cf.pp,
}


def usage():
    pass


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in modules.keys():
        usage()
        sys.exit(1)
    modules[sys.argv[1]].parse_args(sys.argv[1:])


__all__ = ['main']
