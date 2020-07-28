import json

series = 'TNG'
input_file = 'all_series_lines.json'
output_file = 'startrek_tng.csv'

with open(input_file, 'r') as file:
    data = json.load(file)

# print(data[series])

print(f"Processing series {series}")

data = data[series]
all_lines = []
separator = '!'

for episode in data:
    this_ep = data[episode]
    for key, values in this_ep.items():
        if len(values) > 0:
            for value in values:
                line = (f"{key}{separator}{value}")
                all_lines.append(line)

print(f"Writing to {output_file}")
with open(output_file, 'w') as file:
    for line in all_lines:
        file.write(line)
        file.write('\n')

print("Done")
