import csv


with open('names.csv', 'a') as csv_file:
            fieldnames = ['first_name', 'last_name', 'email']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            writer.writerow({'first_name': 'Matt', 'last_name': 'Lope', 'email': 'mover@mover'})