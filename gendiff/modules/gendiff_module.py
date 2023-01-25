from gendiff.modules.stylish import get_stylish


def generate_diff(file_1, file_2, format):
    return get_stylish(file_1, file_2)
