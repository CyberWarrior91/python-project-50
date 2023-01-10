import json, itertools


def generate_diff(file_1, file_2):
    dict_1 = json.load(open(file_1))
    dict_2 = json.load(open(file_2))
    sorted_dict_1 = dict(sorted(dict_1.items(), key=lambda x: x[0]))
    sorted_dict_2 = dict(sorted(dict_2.items(), key=lambda x: x[0]))
    new_list = []
    space = '  '
    for key, value in sorted_dict_1.items():
        if key not in sorted_dict_2:
            new_list.append(f'{space}- {key}: {value}')
        elif key in sorted_dict_2 and value ==  sorted_dict_2[key]:
            new_list.append(f'{space}  {key}: {value}')
        elif key in sorted_dict_2 and value != sorted_dict_2[key]:
            new_list.append(f'{space}- {key}: {value}')
            new_list.append(f'{space}+ {key}: {sorted_dict_2[key]}')
    for key in sorted_dict_2.keys():
         if key not in sorted_dict_1:
              new_list.append(f'{space}+ {key}: {sorted_dict_2[key]}')
    new_string = '\n'.join(itertools.chain('{', new_list, '}'))
    return new_string
    
