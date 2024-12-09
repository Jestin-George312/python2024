print("Name: Jestin George\n ")
print("\n Admission_number: A24MCA035")
print("\n experiment number:15")

try:
    f = open("demofile.txt", "wt")
    f.write("I have created the file \n")
    f.write("The code is working \n")
    f.write("Testing the code \n")
    f.close()

    # Open the file in read mode
    with open('demofile.txt', 'r') as file:
        lines = file.readlines()  # Read all lines into a list

    print(lines)

except Exception as e:
    print(f"some error has occurred {e}")
