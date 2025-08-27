try :
  with open("test.txt","r") as file:
    file.write("Hello PLP Community!")
except FileNotFoundError:
  print("File Not Found! Please Check the file name/directory!")