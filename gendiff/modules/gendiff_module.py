from gendiff.formats.stylish import get_stylish
from gendiff.formats.plain import get_plain
import json
import yaml
from yaml import FullLoader


def open_file(file):
    if file.endswith('json'):
        new_dict = json.load(open(file))
    elif file.endswith('yml') or file.endswith('yaml'):
        new_dict = yaml.load(open(file), Loader=FullLoader)
    else:
        raise Exception(f"File '{file}' is wrong format!")
    return new_dict


def generate_diff(file_1, file_2, format_name='stylish'):
    dict_1 = open_file(file_1)
    dict_2 = open_file(file_2)
    if format_name == 'plain':
        return get_plain(dict_1, dict_2)
    else:
        return get_stylish(dict_1, dict_2)
