import csv

with open('new_names.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
    writer.writerow({'emp_name': 'Adam Knowles', 'dept': 'Nursing', 'birth_month': 'May' })
    writer.writerow({'emp_name': 'Jeremy Davis', 'dept': 'Programming', 'birth_month': 'January' })
    writer.writerow({'emp_name': 'Diana Davis', 'dept': 'Medicine', 'birth_month': 'January' })