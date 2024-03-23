# File Creation
try:
    with open("my_file.txt", 'w') as file:
        file.write("This is line 1\n")
        file.write("2nd line: 12345\n")
        file.write("Line 3: Python file handling\n")
except Exception as e:
    print("Error occurred while creating the file:", e)
finally:
    print("File creation process completed.")

# File Reading and Display
try:
    with open("my_file.txt", 'r') as file:
        file_contents = file.read()
        print("Contents of my_file.txt:")
        print(file_contents)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to read the file.")
except Exception as e:
    print("Error occurred while reading the file:", e)

# File Appending
try:
    with open("my_file.txt", 'a') as file:
        file.write("\nAdditional line 1\n")
        file.write("Extra line 2: 67890\n")
        file.write("Append line 3: Python error handling\n")
except Exception as e:
    print("Error occurred while appending to the file:", e)
finally:
    print("File appending process completed.")
