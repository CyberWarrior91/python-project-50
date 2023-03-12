from json import dumps


def get_json(tree):
    '''Transforms tree in json format'''
    return dumps(tree, indent=4)
