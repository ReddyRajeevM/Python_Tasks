# Task 1: Read a File and Handle Errors 
def openfile(filename):
     try:
          with open(filename,'r') as file1:
               final_output=file1.readlines()
               for i in final_output:
                     print(i)

     except FileNotFoundError:
          print("The file "+filename+" not found.")

print(openfile("sample.txt"))
