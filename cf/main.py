#! /usr/bin/env python3

import sys
import subprocess

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


def execute_external(subcmd, args):
    command = f'cf-{subcmd}'
    subprocess.call([command] + args)


def main():
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)
    subcommand = sys.argv[1]
    if subcommand in modules:
        modules[subcommand].parse_args(sys.argv[1:])
    else:
        execute_external(subcommand, sys.argv[2:])


__all__ = ['main']
