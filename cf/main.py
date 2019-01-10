import argparse
import importlib
import subprocess
import sys


modules = {module: importlib.import_module(f'cf.{module}') for module in [
    'fetch',
    'init',
    'make',
    'pp',
]}


def print_help_and_exit(args):
    args.parser.print_help()
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser()
    parser.set_defaults(parser=parser)
    parser.set_defaults(run=print_help_and_exit)
    subparsers = parser.add_subparsers()

    for name, module in modules.items():
        subparser = subparsers.add_parser(name)
        module.parse_args(subparser)

    args = parser.parse_args()
    args.run(args)


__all__ = ['main']
