#!/usr/bin/python3
"""
Markdown to HTML Converter
"""

from os.path import isfile
import sys
import re
import hashlib


def verify_file_exist(argv):
    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)


def markdown_heading_to_html(lines):
    lines_list = []
    for line in lines:
        for i in range(6, 0, -1):
            if line.startswith('#' * i):
                line = f'<h{i}>{line[i+1:].strip()}</h{i}>\n'
                break
        lines_list.append(line)
    return lines_list


def markdown_ul_to_html(lines):
    lines_list = []
    is_present = False

    for line in lines:
        if line.startswith('- '):
            converted_line = f'<li>{line[2:].strip()}</li>\n'
            if is_present is False:
                lines_list.append('<ul>\n')
                is_present = True
            lines_list.append(converted_line)
        else:
            if is_present is True:
                lines_list.append('</ul>\n')
                is_present = False
            lines_list.append(line)
    if is_present is True:
        lines_list.append('</ul>\n')
    return lines_list


def markdown_ol_to_html(lines):
    lines_list = []
    is_present = False

    for line in lines:
        if line.startswith('* '):
            converted_line = f'<li>{line[2:].strip()}</li>\n'
            if is_present is False:
                lines_list.append('<ol>\n')
                is_present = True
            lines_list.append(converted_line)
        else:
            if is_present is True:
                lines_list.append('</ol>\n')
                is_present = False
            lines_list.append(line)
    if is_present is True:
        lines_list.append('</ol>\n')
    return lines_list


def markdown_paragraph_to_html(lines):
    markdown_list = ('<h', '<ul>', '<li>', '<ol>', '</ul>', '</ol>')
    lines_list = []
    text_list = []

    for line in lines:
        if not line.lstrip().startswith(markdown_list) and line.strip() != '':
            text_list.append(line.strip())
        else:
            if text_list:
                lines_list.append('<p>\n' +
                                  '\n<br/>\n'.join(text_list) + '\n</p>\n')
                text_list = []
            if line.strip() != '':
                lines_list.append(line)
    if text_list:
        lines_list.append('<p>\n' + '\n<br/>\n'.join(text_list) + '\n</p>\n')
    return lines_list


def markdown_bold_to_html_b(lines):
    lines_list = []
    bold = r'\*\*(.+?)\*\*'
    emphasis = r'\_\_(.+?)\_\_'

    for line in lines:
        if '**' in line or '__' in line:
            converted_line = re.sub(bold, r'<b>\1</b>', line)
            converted_line = re.sub(emphasis, r'<em>\1</em>', converted_line)
            lines_list.append(f'{converted_line}')
        elif '__' in line:
            converted_line = re.sub(emphasis, r'<em>\1</em>', line)
            lines_list.append(f'{converted_line}')
        else:
            lines_list.append(line)
    return lines_list


def convert_content_to_MD5(lines):
    lines_list = []
    delimiter = r'\[\[(.+?)\]\]'
    sub1 = str(re.escape('[['))
    sub2 = str(re.escape(']]'))

    for line in lines:
        if '[[' in line:
            content = re.findall(sub1 + "(.*)" + sub2, line.strip())[0]
            content_in_MD5 = hashlib.md5(content.encode("utf")).hexdigest()
            converted_line = re.sub(delimiter, content_in_MD5, line.strip())
            lines_list.append(f'{converted_line}\n')
        else:
            lines_list.append(line)

    return lines_list


def remove_all_c_in_string(lines):
    lines_list = []
    delimiter = r'\(\((.+?)\)\)'
    sub1 = str(re.escape('(('))
    sub2 = str(re.escape('))'))

    for line in lines:
        if '((' in line:
            content = re.findall(sub1 + "(.*)" + sub2, line.strip())[0]
            content_without_c = re.sub('c', '', content, flags=re.IGNORECASE)
            converted_line = re.sub(delimiter, content_without_c, line.strip())
            lines_list.append(f'{converted_line}\n')
        else:
            lines_list.append(line)

    return lines_list


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
        lines = file.readlines()
        html_lines = markdown_heading_to_html(lines)
        html_lines = markdown_ul_to_html(html_lines)
        html_lines = markdown_ol_to_html(html_lines)
        html_lines = markdown_paragraph_to_html(html_lines)
        html_lines = markdown_bold_to_html_b(html_lines)
        html_lines = convert_content_to_MD5(html_lines)
        html_lines = remove_all_c_in_string(html_lines)
        new_file.writelines(html_lines)

    exit(0)


if __name__ == "__main__":
    main()
