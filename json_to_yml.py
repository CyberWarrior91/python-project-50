import json
import yaml

file_1 = json.load(open('tests/fixtures/file2_nested.json'))
file_1 = yaml.dump(file_1)
output_file = open('tests/fixtures/file2_nested.yml', 'w')
output_file.write(file_1)