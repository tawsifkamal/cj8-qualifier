from typing import Any, List, Optional

characters = '│ ─ ┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘'
vertical_bar = characters[0]

def get_max_str(lst, col):
    lst = list(map(list, zip(*lst)))
    return max(lst[col], key=len)

def convert_string(lst):
    str_list = [list(map(str, l)) for l in lst]
    return str_list

def convert_labels(labels):
    str_list = [str(item) for item in labels]
    return str_list

def creating_top_border(num_columns, headers, msg, top_row_ending, horizontal_bar):
    for i in range(num_columns):
        headers.append(f'{characters[6]}{horizontal_bar[i]}')
    
    for i in range(len(headers) - 1):
        msg += headers[i + 1]
    
    msg += f'{top_row_ending}\n'

    return msg

def spacing_logistics(longest_string_column, item, x):
    spacing_bin = (len(longest_string_column[x]) + 2 - len(item)) / 2
    if spacing_bin - int(spacing_bin) == 0:
        spacing_bin = int(spacing_bin) 
        spacing_left = " " * spacing_bin
        spacing_right = spacing_left
    else: 
        spacing_bin = int(spacing_bin - 0.5)
    
        spacing_left = " " * spacing_bin
        spacing_right = " " * (spacing_bin + 1)

    return spacing_left, spacing_right

def header_creation(centered, empty_labels, longest_string_column, x, item):
    if centered == True:
        spacing_left, spacing_right = spacing_logistics(longest_string_column, item, x)
        empty_labels.append(f'{vertical_bar}{spacing_left}{item}{spacing_right}')
    else: 
        spacing = len(longest_string_column[x]) - len(item) + 1
        empty_labels.append(f'{vertical_bar} {item}{" " * spacing}')



def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    rows = convert_string(rows)
    num_columns = len(rows[0])
    longest_string_column = []
    horizontal_bar = []
    headers = []
    empty_labels = []

    # header creation
    for column in range(num_columns):
        longest_string_column.append(get_max_str(rows, column))


    if labels is not None:
        labels = convert_labels(labels)
        for column in range(len(longest_string_column)):
            if len(labels[column]) > len(longest_string_column[column]):
                longest_string_column[column] = labels[column]
            horizontal_bar.append(characters[2] * (len(longest_string_column[column]) + 2))
        
        msg = f'{characters[4]}{horizontal_bar[0]}'
        top_row_ending = f'{characters[8]}'
        msg = creating_top_border(num_columns, headers, msg, top_row_ending, horizontal_bar)

        for x, label in enumerate(labels):
            if len(label) > len(longest_string_column[x]):
                longest_string_column[x] = label
            header_creation(centered, empty_labels, longest_string_column, x, label)
        
        for x in range(len(empty_labels)):
            msg += empty_labels[x]
            if x - len(empty_labels) + 1 == 0:
                msg += f'{vertical_bar}\n'
        
        horizontal_bar_labels = '┼'.join(horizontal_bar)
        ending_labels = f'{characters[10]}{horizontal_bar_labels}{characters[14]}\n'
        msg += ending_labels
    
    else:
        for column in range(len(longest_string_column)):
            horizontal_bar.append(characters[2] * (len(longest_string_column[column]) + 2))
        msg = f'{characters[4]}{horizontal_bar[0]}'
        top_row_ending = f'{characters[8]}'
        msg = creating_top_border(num_columns, headers, msg, top_row_ending, horizontal_bar)


    # table body creation
    for sublist in rows:
        empty = []
        for x, word in enumerate(sublist):
            header_creation(centered, empty, longest_string_column, x, word)

        for x in range(len(empty)):
            msg += empty[x]
            if x - len(empty) + 1 == 0:
                msg += f'{vertical_bar}\n'
                   
    horizontal_bar = '┴'.join(horizontal_bar)
    ending = f'{characters[16]}{horizontal_bar}{characters[20]}'
    msg += ending
    return msg

