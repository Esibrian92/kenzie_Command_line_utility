#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Erick Sibrian, Joseph hafed,Daniel"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description="creates an instance of the parser")
    """add argument """
    parser.add_argument(
        "-u", "--upper", help="convert text to uppercase", action="store_true")
    parser.add_argument(
        "-l", "--lower", help="convert text to lowercase", action="store_true")
    parser.add_argument(
        "-t", "--title", help="convert text to titlecase", action="store_true")
    parser.add_argument("text", type=str, help="text to be manipulated")
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    # argument conditions

    result = ns.text
    if ns.upper:
        result = ns.text.upper()
    if ns.lower:
        result = ns.text.lower()
    if ns.title:
        result = ns.text.title()
    print(result)


if __name__ == '__main__':
    main(sys.argv[1:])
