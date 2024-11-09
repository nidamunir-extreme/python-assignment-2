import csv

def average_grades(csv_filename):
    with open(csv_filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            grades = [float(value) for key, value in row.items() if key != 'Name']
            average = sum(grades) / len(grades)
            print(f"{row['Name']} - Average grade: {average:.2f}")


average_grades('students.csv')
