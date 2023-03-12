import json
import yaml


def parse(file, extension):
    '''
    Parses data from path in command line and transforms it
    into Python dictionary
    '''
    if extension == 'json':
        return json.load(file)
    elif extension in ('yml', 'yaml'):
        return yaml.safe_load(file)
    else:
        raise Exception(f"File '{file}' is wrong format!")
