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


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    for name, module in modules.items():
        subparser = subparsers.add_parser(name)
        module.parse_args(subparser)

    args = parser.parse_args()
    args.run(args)


__all__ = ['main']
