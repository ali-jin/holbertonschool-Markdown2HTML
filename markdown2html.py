#!/usr/bin/python3
"""scritp that convert markdown to html"""
from os.path import isfile
import sys


def markdown_to_html(argv):
    """Convert markdown in file into html

    argv (str): 2 arguments:
                        - first is the input file name
                        - the second is ouput file name
    """
    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    if isfile(argv[1]) is False:
        print("Missing <filename>", file=sys.stderr)
        exit(1)

    exit(0)


if __name__ == "__main__":
    markdown_to_html(sys.argv)
