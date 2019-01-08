#! /usr/bin/env python3

import argparse
import sys
import subprocess
import importlib


modules = { module: importlib.import_module(f'cf.{module}') for module in [
    'fetch',
    'init',
    'make',
    'pp',
]}


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
