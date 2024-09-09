import csv

airports = r"C:\Users\tio\Documents\airports.csv"
with open(r'C:\Users\tio\Documents\airports.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    for airport in reader:

        if airport['iso_country'] == 'UA':
            print(airport['name'])
