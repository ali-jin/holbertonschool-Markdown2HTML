#!/usr/bin/python3
"""
Markdown to HTML Converter
task 0
"""

from os.path import isfile
import sys


def verify_file_exist(argv):
    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    if isfile(argv[1]) is False:
        print("Missing " + argv[1], file=sys.stderr)
        exit(1)


def markdown_to_html(line):
    for i in range(6, 0, -1):
        if line.startswith('#' * i):
            return f'<h{i}>{line}'


def main():
    """
    Convert the markdown in file into HTML in a new file

    Verify if file exist and if there are enough arguments
    """
    verify_file_exist(sys.argv)
    exit(0)


if __name__ == "__main__":
    main()
