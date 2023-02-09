import itertools
from gendiff.modules.key_generator import generate_uniq_keys_set


def diff_for_mutual_keys(key, dict_1, dict_2, space_count):
    diff_list = []
    if dict_1[key] == dict_2[key]:
        pass
    else:
        diff_list.append(
            f"Property '{key}' was updated. From "
            f"{check_data_type(dict_1[key])} to "
            f"{check_data_type(dict_2[key])}")
    return diff_list


def diff_for_different_keys(key, dict_1, dict_2, space_count):
    diff_list = []
    if key not in dict_2:
        diff_list.append(f"Property '{key}' was removed")
    else:
        diff_list.append(f"Property '{key}' "
                         f"was added with value: "
                         f"{check_data_type(dict_2[key])}")
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


def check_data_type(value):
    if isinstance(value, bool) or value == 'null':
        return f"{str(value).lower()}"
    if value == '[complex value]' or not isinstance(value, str):
        return f"{value}"
    else:
        return f"'{str(value).lower()}'"


def create_new_dict(dictionary_1, dictionary_2):
    new_dict = {}
    for key in dictionary_1.keys():
        if key in dictionary_2:
            empty_dict = {}
            initial_value = key
            new_dict[key] = making_str_keys(
                dictionary_1[key], dictionary_2[key], initial_value, empty_dict)
        else:
            new_dict[key] = {}
    return new_dict


def diff_key_list(dict_1, dict_2):
    diff_list = []
    for key in dict_1.keys():
        if key not in dict_2 and isinstance(dict_1[key], dict):
            diff_list.append(f"Property '{key}' was removed")
    for key in dict_2.keys():
        if key not in dict_1.keys() and isinstance(dict_2[key], dict):
            diff_list.append(
                f"Property '{key}' "
                f"was added with value: [complex value]")
    return diff_list


def making_str_keys(dict_1, dict_2, initial_value, new_dict):
    new_value = initial_value
    for key, v in dict_1.items():
        if isinstance(v, dict):
            if key != initial_value:
                new_value = f'{initial_value}.{key}'
                if key in dict_2 and not isinstance(dict_2[key], dict) \
                   or key not in dict_2:
                    new_dict[new_value] = '[complex value]'
                else:
                    making_str_keys(v, dict_2[key], new_value, new_dict)
        else:
            if v is None:
                v = 'null'
            new_dict[f'{initial_value}.{key}'] = v
    return new_dict


def make_tree_for_dict(dict_1, dict_2):
    diff_list = []
    for key in dict_1.keys():
        if isinstance(dict_1[key], dict):
            new_dict_1 = create_new_dict(dict_1, dict_2)
            new_dict_2 = create_new_dict(dict_2, dict_1)
            diff_list_1 = making_diff(
                new_dict_1[key], new_dict_2.get(key, {}),
                space_count='')
            diff_list.extend(diff_list_1)
        else:
            diff_list = making_diff(dict_1, dict_2, space_count='')
    return diff_list


def get_plain(dict_1, dict_2):
    diff_list = diff_key_list(dict_1, dict_2)
    diff_list.extend(make_tree_for_dict(dict_1, dict_2))
    diff_string = itertools.chain(sorted(diff_list))
    return '\n'.join(diff_string)
