#!/usr/bin/python3
"""
Markdown to HTML Converter
"""

from os.path import isfile
import sys


def verify_file_exist(argv):

    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)


def markdown_to_html(line):
    for i in range(6, 0, -1):
        if line.startswith('#' * i):
            return f'<h{i}>{line[i+1:].strip()}<h{i}>\n'
    return line


def main():
    """Convert the markdown in file into HTML in a new file

    Verify if file exist and if there are enough
    """
    verify_file_exist(sys.argv)

    markdown_file = sys.argv[1]

    if isfile(markdown_file) is False:
        print("Missing " + markdown_file, file=sys.stderr)
        exit(1)

    with open(markdown_file, 'r') as file, open(sys.argv[2], 'w') as new_file:
        for line in file:
            html_string = markdown_to_html(line)
            new_file.write(html_string)

    exit(0)


if __name__ == "__main__":
    main()
