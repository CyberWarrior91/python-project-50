import json


def generate_uniq_keys_set(dict_1, dict_2):
    result = set()
    for key in dict_1.keys():
        result.add(f'{key}')
    for key in dict_2.keys():
        result.add(f'{key}')
    return sorted(result)


def making_diff(dict_1, dict_2, space_count):
    if isinstance(dict_1, dict) and isinstance(dict_2, dict):
        dict_set = generate_uniq_keys_set(dict_1, dict_2)
    else:
        if isinstance(dict_1, dict):
            dict_set = generate_uniq_keys_set(dict_1, dict_1)
        else:
            dict_set = generate_uniq_keys_set(dict_2, dict_2)
    diff_dict = {}
    for key in dict_set:
        if key in dict_1 and key in dict_2:
            diff_dict[key] = (
                diff_for_mutual_keys(key, dict_1, dict_2, space_count)
            )
        else:
            diff_dict[key] = (
                diff_for_different_keys(key, dict_1, dict_2, space_count)
            )
    return diff_dict


def diff_for_mutual_keys(key, dict_1, dict_2, space_count):
    diff_dict = {}
    diff_dict['key'] = key
    if dict_1[key] == dict_2[key]:
        diff_dict["type"] = 'stayed'
    if isinstance(dict_1[key], dict) and isinstance(dict_2[key], dict):
        diff_dict["value"] = dict_1[key]
    elif dict_1[key] != dict_2[key]:
        diff_dict["type"] = 'changed value'
        diff_dict["value1"] = dict_1[key]
        diff_dict["value2"] = dict_2[key]
    return diff_dict


def diff_for_different_keys(key, dict_1, dict_2, space_count):
    diff_dict = {}
    diff_dict["key"] = key
    if not dict_2 or isinstance(dict_2, str):
        diff_dict["value"] = dict_1[key]
    elif key not in dict_2:
        diff_dict["type"] = 'deleted'
        diff_dict["value"] = dict_1[key]
    else:
        diff_dict["type"] = 'added'
        diff_dict["value"] = dict_2[key]
    return diff_dict


def get_json(dict_1, dict_2):
    json_dict = {}
    new_dict = {}
    json_dict["type"] = 'root'
    new_dict = make_tree_for_dict(dict_1, dict_2)
    json_dict["children"] = new_dict
    return json.dumps(json_dict, indent=3)


def make_tree_for_dict(dict_1, dict_2):
    for key in dict_1.keys():
        if isinstance(dict_1[key], dict):
            dict_1[key] = make_tree_for_dict(dict_1[key], dict_2.get(key, {}))
    dict_1 = making_diff(dict_1, dict_2, space_count='')
    return dict_1
