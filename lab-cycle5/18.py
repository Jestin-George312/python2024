print("Name: Jestin George\n ")
print("\n Admission_number: A24MCA035")
print("\n experiment number:18")

try:
    import csv
    csv_file = 'one_csv.csv'
    columns_to_read = [0, 2]

    with open(csv_file, mode='r', newline='') as file:

        csv_reader = csv.reader(file)
        selected_columns = []

        for row in csv_reader:
            selected_columns.append([row[i] for i in columns_to_read])

        print(selected_columns)

except Exception as e:
    print(f"\nAn error occurred: {e}")
