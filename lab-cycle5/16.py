print("Name: Jestin George\n ")
print("\n Admission_number: A24MCA035")
print("\n experiment number:16")

try:
    print()
    with open("demofile.txt", 'rt') as src:
        with open("demofile2.txt", 'wt') as dest:
            # Iterate through lines with their line number
            for line_number, line in enumerate(src, start=1):
                if line_number % 2 != 0:  # Check if the line number is odd
                    dest.write(line)  # Write the odd lines to destination file
    print("Odd lines have been copied successfully.")
except FileNotFoundError:
        print(f"Error: The file '{src}' does not exist.")
except Exception as e:
    print(f"some error happened {e}")