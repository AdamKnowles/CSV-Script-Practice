import csv

with open('names.csv', 'r') as new_file:
    csv_reader = csv.reader(new_file)

        
    for taco in csv_reader:
        print(taco)

