import csv

with open('names.csv', mode='w') as csv_file:
    fieldnames = ['first_name', 'last_name', 'email']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'John', 'last_name': 'Smith', 'email': 'November@november'})
    writer.writerow({'first_name': 'Erica', 'last_name': 'Knowles', 'email': 'March@november'})
    writer.writerow({'first_name': 'Adam', 'last_name': 'Yentzer', 'email': 'May@may'})
    writer.writerow({'first_name': 'Jeremy', 'last_name': 'Davis', 'email': 'January@january'})
    writer.writerow({'first_name': 'Diana', 'last_name': 'Davis', 'email': 'January@january'})

        

