#! /usr/bin/env python3

import argparse
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


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    for name, module in modules.items():
        subparser = subparsers.add_parser(name)
        module.parse_args(subparser)

    args = parser.parse_args()
    args.run(args)


__all__ = ['main']
