import json
import yaml
from yaml import FullLoader
import itertools


def making_list(dict_1, dict_2, space_count):
    new_list = []
    for key, value in dict_1.items():
        if key not in dict_2:
            new_list.append(f'{space_count}- {key}: {str(value).lower()}')
        elif key in dict_2 and value == dict_2[key]:
            new_list.append(f'{space_count}  {key}: {str(value).lower()}')
        elif key in dict_2 and isinstance(dict_1[key], str):
            new_list.append(f'{space_count}  {key}: {value}')
        else:
            new_list.append(f'{space_count}- {key}: {str(value).lower()}')
            new_list.append(f'{space_count}+ {key}: {str(dict_2[key]).lower()}')
    if isinstance(dict_2, dict):
        for key in dict_2.keys():
            if key not in dict_1:
                new_list.append(f'{space_count}+ {key}: {str(dict_2[key]).lower()}')
    print(new_list)
    return sorted(new_list)


def open_file(file):
    if file.endswith('json'):
        new_dict = json.load(open(file))
    elif file.endswith('yml') or file.endswith('yaml'):
        new_dict = yaml.load(open(file), Loader=FullLoader)
    else:
        raise Exception(f"File '{file}' is wrong format!")
    return new_dict


def generate_diff(file_1, file_2):
    dict_1 = open_file(file_1)
    dict_2 = open_file(file_2)
    def walk(dict_1, dict_2, depth):
        space = '  '
        space_count = space * depth
        print(dict_1)
        print(dict_2)
        for key, _ in dict_1.items():
            if isinstance(dict_1[key], dict):
                dict_1[key] = walk(dict_1[key], dict_2.get(key, {}), depth + 2)
        
        new_list = making_list(dict_1, dict_2, space_count)
        new_string = itertools.chain('{', new_list, [space_count + '}'])
        return '\n'.join(new_string)
    return walk(dict_1, dict_2, depth=0)

print(generate_diff('tests/fixtures/file_3.json', 'tests/fixtures/file_4.json'))