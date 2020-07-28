import json

series = 'TNG'
input_file = 'all_series_lines.json'
output_file = 'startrek_tng.csv'

with open(input_file, 'r') as file:
    data = json.load(file)

# print(data[series])

data = data[series]
all_lines = []
separator = '!'

for episode in data:
    this_ep = data[episode]
    for key, values in this_ep.items():
        if len(values) > 0:
            # print(f"{key}: {values}")
            for value in values:
                line = (f"{key}{separator}{value}")
                all_lines.append(line)

print(all_lines)

for line in all_lines:
    print(line)

with open(output_file, 'w') as file:
    for line in all_lines:
        file.write(line)
        file.write('\n')
