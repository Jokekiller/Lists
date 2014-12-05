#Harry Robinson
#05-12-2014
#storing names

name1 = str(input("Enter the first name: "))
name2 = str(input("Enter the second name: "))
name3 = str(input("Enter the third name: "))
name4 = str(input("Enter the fourth name: "))
name5 = str(input("Enter the fifth name: "))
name6 = str(input("Enter the sixth name: "))
name7 = str(input("Enter the seventh name: "))
name8 = str(input("Enter the eigth name: "))
nameList = [name1, name2, name3, name4, name5, name6, name7, name8]
for each in nameList:
    print(each)
studentToChange = str(input("Enter the new student name: "))
placeToChange = int(input("Enter where this student needs to be replaced: "))
nameList.insert(placeToChange,studentToChange)
for each in nameList:
    print(each)
