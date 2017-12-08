import sys


def _emit(elements, separator='\t'):
    # convert all list items to string
    # by appling function str to all list items using function map
    elements_as_string = map(str, elements)
    # concatenation all list items by separator to one string
    output_string = separator.join(elements_as_string)
    print(output_string)


def split(line: str, separator=',') -> []:
    return line.split(sep=separator)


def __map():
    for line in sys.stdin:
        cols = split(line)
        if __is_ign_review(cols):
            # since its an ign review
            # get the columns title(2), platform(4), score(5)
            title, platform, score = cols[2], cols[4], cols[5]
            _emit([title, platform, score])

        else:
            # since its a sales statement
            # get the columns title(1), platform(2), sales(10)
            title, platform, sales, data_type = cols[1], cols[2], cols[10], "S"
            _emit([title, platform, sales, data_type])


def __is_ign_review(cols: []):
    return not cols[3].isdigit()


if __name__ == '__main__':
    __map()
