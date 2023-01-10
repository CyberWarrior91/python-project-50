import json, itertools

def generate_diff(file_1, file_2):
    dict_1 = json.load(open(file_1))
    dict_2 = json.load(open(file_2))
    sorted_dict_1 = dict(sorted(dict_1.items(), key=lambda x: x[0]))
    sorted_dict_2 = dict(sorted(dict_2.items(), key=lambda x: x[0]))
    new_list = []
    for key, value in sorted_dict_1.items():
        if key not in sorted_dict_2:
            new_list.append(f'- {key}: {value}')
        elif key in sorted_dict_2 and value ==  sorted_dict_2[key]:
            new_list.append(f'  {key}: {value}')
        elif key in sorted_dict_2 and value != sorted_dict_2[key]:
            new_list.append(f'- {key}: {value}')
            new_list.append(f'+ {key}: {sorted_dict_2[key]}')
    for key in sorted_dict_2.keys():
         if key not in sorted_dict_1:
              new_list.append(f'+ {key}: {sorted_dict_2[key]}')
    new_string = '\n'.join(itertools.chain('{', new_list, '}'))
    print(new_string)
    

generate_diff('gendiff/modules/file1.json', 'gendiff/modules/file2.json')