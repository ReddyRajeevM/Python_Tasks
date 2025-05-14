# Task 1: Create a Dictionary of Student Marks

studentname= input('Please enter the student name: ').capitalize()
if studentname.isalpha:
    def Results(studentname):
        studentmarks= {'Vikas':76, 'Sandeep': 89,'Vijay':55,'Satya':96}
        studentvalidation=(studentname in studentmarks)
        print('Student found: {}'.format(studentvalidation))
        if studentvalidation==True:
            Marks= studentmarks[studentname]
            print("{}'s marks: {}".format(studentname, Marks))
        else:
            print("'{}' student NOT FOUND".format(studentname))

    print(Results(studentname))
    
else:
    print("Invalid Entey. Please enter only Alphabets.")
