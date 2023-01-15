import json
import yaml
from yaml import FullLoader
import itertools


def making_list(dict_1, dict_2):
    new_list = []
    space = '  '
    for key, value in dict_1.items():
        if key not in dict_2:
            new_list.append(f'{space}- {key}: {str(value).lower()}')
        elif key in dict_2 and value == dict_2[key]:
            new_list.append(f'{space}  {key}: {str(value).lower()}')
        else:
            new_list.append(f'{space}- {key}: {str(value).lower()}')
            new_list.append(f'{space}+ {key}: {str(dict_2[key]).lower()}')
    for key in dict_2.keys():
        if key not in dict_1:
            new_list.append(f'{space}+ {key}: {str(dict_2[key]).lower()}')
    return new_list


def open_file(file_1, file_2):
    if file_1.endswith('json'):
        dict_1 = json.load(open(file_1))
        dict_2 = json.load(open(file_2))
    else:
        dict_1 = yaml.load(open(file_1), Loader=FullLoader)
        dict_2 = yaml.load(open(file_2), Loader=FullLoader)
    return dict_1, dict_2


def generate_diff(file_1, file_2):
    dict_1, dict_2 = open_file(file_1, file_2)
    sorted_dict_1 = dict(sorted(dict_1.items(), key=lambda x: x[0]))
    sorted_dict_2 = dict(sorted(dict_2.items(), key=lambda x: x[0]))
    new_list = making_list(sorted_dict_1, sorted_dict_2)
    new_string = '\n'.join(itertools.chain('{', new_list, '}'))
    return new_string
