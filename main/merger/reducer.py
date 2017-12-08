#!/usr/bin/env python

import sys


def _format_and_split(line, separator=','):
    # remove leading and trailing whitespace and split on separator
    return line.strip().split(separator)


def _emit(elements, separator=','):
    # convert all list items to string
    # by appling function str to all list items using function map
    elements_as_string = map(str, elements)
    # concatenation all list items by separator to one string
    output_string = separator.join(elements_as_string)
    print(output_string)


def _title_changed(title_of_previous_line, title_of_current_line):
    return title_of_previous_line and (title_of_previous_line != title_of_current_line)


def is_review(cols):
    return len(cols) == 2


def reduce():
    title_sales = 0
    title_score = 0
    count = 0
    last_title = None

    for line in sys.stdin:
        # parse the input we got from mapper.py
        cols = _format_and_split(line)
        if _title_changed(last_title, cols[0]):
            # make sure of no missing data
            if title_score != 0 and title_sales != 0:
                # get average of score
                _emit([last_title, title_score/count, title_sales])
            title_sales = 0
            title_score = 0
            count = 0

        if is_review(cols):
            title_score += float(cols[1])
            count += 1
        else:
            title_sales += float(cols[2])
        last_title = cols[0]


if __name__ == '__main__':
    reduce()
