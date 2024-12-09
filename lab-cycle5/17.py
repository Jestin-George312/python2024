import csv
print("Name: Jestin George\n ")
print("\n Admission_number: A24MCA035")
print("\n experiment number:17")

try:
    with (open("one_csv.csv",'r') as file):
       csvFile = csv.reader(file)
       for index,lines in enumerate(csvFile):
        print(f"{index}:{lines}")
except Exception as e :
    print(f"Some error has occurred {e}")