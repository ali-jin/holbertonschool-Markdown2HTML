#!/usr/bin/python3
"""
Markdown to HTML Converter
Task 1: convert heading
"""
from os.path import isfile
import sys
import markdown


def verify_file_exist(argv):
    """Verify if file exist

    argv (str): 2 arguments string
    """
    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    if isfile(argv[1]) is False:
        print("Missing " + argv[1], file=sys.stderr)
        exit(1)


def markdown_to_html(argv):
    """Convert markdown in file into html

    argv (str): 2 arguments string
    """
    with open(argv[1], 'r') as file:
        markdown_string = file.read()

    html_string = markdown.markdown(markdown_string)

    with open(argv[2], 'w') as new_file:
        new_file.write(html_string)


if __name__ == "__main__":
    verify_file_exist(sys.argv)
    markdown_to_html(sys.argv)
