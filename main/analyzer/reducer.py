#!/usr/bin/env python

import sys


def _format_and_split(line, separator='\t'):
    # remove leading and trailing whitespace and split on separator
    return line.strip().split(separator)


def _emit(elements, separator='\t'):
    # convert all list items to string
    # by appling function str to all list items using function map
    elements_as_string = map(str, elements)
    # concatenation all list items by separator to one string
    output_string = separator.join(elements_as_string)
    print(output_string)


def _score_changed(score_of_previous_line, score_of_current_line):
    return score_of_current_line and (score_of_previous_line != score_of_current_line)


def is_review(cols):
    return len(cols) == 2


def _reduce():
    score_sales = 0
    last_score = 1
    count = 0
    for line in sys.stdin:
        cols = _format_and_split(line)
        score = int(float(cols[0]))
        if _score_changed(last_score, score):
            # get the the score sales mean
            _emit([last_score, score_sales / count])
            score_sales = 0
            count = 0
        # accumulate the sales in order to get the mean at last
        score_sales += float(cols[1])

        last_score = score
        count += 1
    _emit([last_score, score_sales/count])


if __name__ == '__main__':
    _reduce()
