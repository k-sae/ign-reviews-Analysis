#!/usr/bin/env python

import sys


def _emit(elements, separator='\t'):
    # convert all list items to string
    # by appling function str to all list items using function map
    elements_as_string = map(str, elements)
    # concatenation all list items by separator to one string
    output_string = separator.join(elements_as_string)
    print(output_string)


def split(line, separator=','):
    return line.strip().split(separator)


def __map():
    for line in sys.stdin:
        cols = split(line)
        # since its an ign review
        # get the columns title(0), score(1), sales(2)
        _, score, sales = cols
        _emit([score, sales])


def __is_ign_review(cols):
    return not cols[3].isdigit()


if __name__ == '__main__':
    __map()
