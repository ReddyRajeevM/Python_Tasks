# Task 2: Demonstrate List Slicing 

RequiredElementCount=input("Please enter the number of elements to extract: ")
List1=[1,2,3,4,5,6,7,8,9,10]
requiredList=List1[0:int(RequiredElementCount)]
print('Extracted first {} elements: {}'.format(RequiredElementCount, requiredList))

#Reversing the extracted list
requiredList.reverse()
print('Reversed elements list: {}'.format(requiredList))


