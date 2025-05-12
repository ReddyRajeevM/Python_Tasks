#Task 2: Write and Append Data to a File

def writeAndappend(filename):
     try:
          userinput=input("Enter the text you want to write: ")
          with open(filename,'w') as file1:
               final_output=file1.write(userinput+"\n")

          file1 = open(filename,'a')
          final_output=file1.write("Data appended successfully.\n")
          file1.close()

     except FileNotFoundError:
          print("The file "+filename+" not found.")

print(writeAndappend("output.txt"))
