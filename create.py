import csv

data = [
    ['Category', 'Value'],
    ['Python', 40],
    ['Java', 20],
    ['JavaScript', 15],
    ['C++', 15],
    ['C', 10]
]

filename = 'data.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f'{filename} created successfully.')
