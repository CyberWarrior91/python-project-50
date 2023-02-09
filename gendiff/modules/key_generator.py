def generate_uniq_keys_set(dict_1, dict_2):
    result = set()
    for key in dict_1.keys():
        result.add(f'{key}')
    for key in dict_2.keys():
        result.add(f'{key}')
    return sorted(result)
