import itertools
from gendiff.modules.key_generator import generate_uniq_keys_set


def diff_for_mutual_keys(key, dict_1, dict_2, space_count):
    diff_list = []
    if dict_1[key] == dict_2[key]:
        diff_list.append(f'{space_count}  {key}: {dict_1[key]}')
    elif "\n" and "-" in str(dict_1[key]) and isinstance(dict_2[key], dict):
        diff_list.append(f'{space_count}  {key}: {dict_1[key]}')
    else:
        diff_list.append(f'{space_count}- {key}: {str(dict_1[key]).lower()}')
        diff_list.append(f'{space_count}+ {key}: {str(dict_2[key]).lower()}')
    return diff_list


def diff_for_different_keys(key, dict_1, dict_2, space_count):
    diff_list = []
    if key in dict_1 and not dict_2 or isinstance(dict_2, str):
        diff_list.append(f'{space_count}  {key}: {dict_1[key]}')
    elif key not in dict_2:
        diff_list.append(f'{space_count}- {key}: {str(dict_1[key]).lower()}')
    elif key in dict_2 and not dict_1 or isinstance(dict_1, str):
        diff_list.append(f'{space_count}  {key}: {dict_2[key]}')
    else:
        diff_list.append(f'{space_count}+ {key}: {str(dict_2[key]).lower()}')
    return diff_list


def making_diff(dict_1, dict_2, space_count):
    if isinstance(dict_1, dict) and isinstance(dict_2, dict):
        dict_set = generate_uniq_keys_set(dict_1, dict_2)
    else:
        dict_set = dict_set_for_str_values(dict_1, dict_2)
    diff_list = []
    for key in dict_set:
        if key in dict_1 and key in dict_2:
            diff_list.extend(
                diff_for_mutual_keys(key, dict_1, dict_2, space_count)
            )
        else:
            diff_list.extend(
                diff_for_different_keys(key, dict_1, dict_2, space_count)
            )
    return diff_list


def dict_set_for_str_values(dict_1, dict_2):
    if isinstance(dict_1, dict):
        dict_set = generate_uniq_keys_set(dict_1, dict_1)
    else:
        dict_set = generate_uniq_keys_set(dict_2, dict_2)
    return dict_set


def make_tree_for_dict_1(dict_1, dict_2, depth, walk):
    for key in dict_1.keys():
        if dict_1[key] is None:
            dict_1[key] = 'null'
        elif isinstance(dict_1[key], dict):
            dict_1[key] = walk(dict_1[key], dict_2.get(key, {}), depth + 2)


def make_tree_for_dict_2(dict_1, dict_2, depth, walk):
    for key in dict_2.keys():
        if dict_2[key] is None:
            dict_2[key] = 'null'
        if isinstance(dict_2[key], dict) and \
           isinstance(dict_1.get(key, {}), bool):
            dict_2[key] = walk({}, dict_2[key], depth + 2)
        elif isinstance(dict_2[key], dict) and '-' not in dict_1.get(key, {}):
            dict_2[key] = walk(dict_1.get(key, {}), dict_2[key], depth + 2)


def get_stylish(dict_1, dict_2):
    def walk(dict_1, dict_2, depth):
        if isinstance(dict_1, dict):
            make_tree_for_dict_1(dict_1, dict_2, depth, walk)
        if isinstance(dict_2, dict) and isinstance(dict_1, dict):
            make_tree_for_dict_2(dict_1, dict_2, depth, walk)
        space = '  '
        space_count = space * depth
        closing_space = space * (depth - 1)
        diff_list = making_diff(dict_1, dict_2, space_count)
        diff_string = itertools.chain(
            '{', diff_list, [closing_space + '}']
        )
        return '\n'.join(diff_string)
    return walk(dict_1, dict_2, depth=1)
