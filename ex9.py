import csv

def read_csv(file_name):

    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            data_exists = False

            for row in reader:
                name = row["name"]
                age = row["age"]
                print("Name:", name)
                print("Age:", age)
                print()
                data_exists = True

            if not data_exists:
                print("No data found.")
            
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

read_csv("students.csv")
