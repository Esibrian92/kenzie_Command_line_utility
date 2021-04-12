#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Erick Sibrian, Joseph hafed"


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
    print(type(ns))
    if not ns:
        parser.print_usage()
        sys.exit(1)

    # argument conditions

    if ns.upper:
        print(ns.text.upper())
    elif ns.title:
        print(ns.text.title())
    elif ns.lower:
        print(ns.lower())
    return


if __name__ == '__main__':
    main(sys.argv[1:])
