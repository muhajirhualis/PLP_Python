""" 
1. File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.

"""

def file_read_write():
  with open("test.txt", "r+") as file:
    content = file.read()
    print(content)
    
  with open("mod_test.txt", "w+") as file2:
    modified_content = content.upper()
    file2.write(modified_content)
    
file_read_write()


""" 
2. Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

"""
filename = input(" Enter the filename:")
try:
  with open(filename,"r") as file:
    Content = file.read()
    print(f"File {filename} Exists and Here is Content:\n")
    print(Content)
except FileNotFoundError:
  print("File {filename} Doesn't Exists or can’t be read")
except PermissionError:
  print(f"Error: You do not have permission to read the file '{filename}'")
except Exception as e:
    print(f"An unexpected error occurred: {e}.")
  
    