#!/usr/bin/python3
"""scritp that convert markdown to html"""
from os.path import isfile
import sys
import markdown


def verify_file_exist(argv):
    """Verify if file exist

    argv (str): 2 arguments:
                        - first is the input file name
                        - the second is ouput file name
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

    argv (str): 2 arguments:
                        - first is the input file name
                        - the second is ouput file name
    """
    with open(argv[1], 'r') as file:
        markdown_string = file.read()

    htmk_string = markdown.markdown(markdown_string)

    with open(argv[2], 'w') as new_file:
        new_file.write(htmk_string)


if __name__ == "__main__":
    """main"""
    verify_file_exist(sys.argv)
    markdown_to_html(sys.argv)
