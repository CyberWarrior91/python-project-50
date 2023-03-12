def build_plain(node, ancestry='') -> str:
    """
    starts comparing children inside the root nodes
    :return: string of comparisons
    """
    str_key = f'{ancestry}{node.get("key")}'
    children = node.get('children')
    if node['type'] == 'root':
        lines = map(lambda child: build_plain(child), children)
        result = sum(lines, [])
        return '\n'.join(result)
    elif node['type'] == 'added':
        return [f"Property '{str_key}' was added with value: "
                f"{check_data_type(node['value'])}"]
    elif node['type'] == 'deleted':
        return [f"Property '{str_key}' was removed"]
    elif node['type'] == 'changed':
        return [
            f"Property '{str_key}' was updated. From "
            f"{check_data_type(node['value1'])} to "
            f"{check_data_type(node['value2'])}"
        ]
    elif node['type'] == 'unchanged':
        return []
    elif node['type'] == 'nested':
        ancestry = node['key']
        lines = map(lambda child: build_plain(child, f"{str_key}."), children)
        return sum(lines, [])
    else:
        raise Exception(f"{node['type']} is a wrong type!")


def check_data_type(value):
    '''Checking type of data which comes from the tree'''
    if isinstance(value, bool) or isinstance(value, int):
        return f"{str(value).lower()}"
    elif value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    else:
        return f"'{str(value).lower()}'"


def get_plain(tree):
    return build_plain(tree)
