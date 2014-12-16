#Harry Robinson
#15-12-2014
#Name program

nameList = []
for name in range (6):
    names = input("Enter a name: ")
    nameList.append(names)
for name in nameList:
    print(name)
name_range = int(input("Enter a range value 1: "))
name_range2 = int(input("Enter a range value 2: "))
range_of_names = nameList[name_range, name_range2]
print(range_of_names)
