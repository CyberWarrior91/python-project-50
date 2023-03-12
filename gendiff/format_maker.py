from gendiff.formats.stylish import get_stylish
from gendiff.formats.plain import get_plain
from gendiff.formats.json import get_json
from gendiff.modules.tree import make_tree
from gendiff.parser import parse


def open_file(path):
    '''
    Gets data from the parse function and opens relevant file
    in the working directory.
    '''
    return parse(open(path), path.split('.')[-1])


def generate_diff(file_1, file_2, format_name='stylish'):
    '''
    Compares two dictionaries and returns the difference
    depending on chosen format.
    '''
    old_dict = open_file(file_1)
    new_dict = open_file(file_2)
    tree = make_tree(old_dict, new_dict)
    if format_name == 'plain':
        return get_plain(tree)
    if format_name == 'json':
        return get_json(tree)
    if format_name in ('stylish', None):
        return get_stylish(tree)
    else:
        raise Exception(f"The format {format_name} "
              f"is wrong and cannot be executed.")
