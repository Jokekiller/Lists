#Harry Robinson
#19-12-2014
#Student name and date of birth

student = []
date_of_birth = []
count = 1
def student_details():        
    name = input("Enter the student name: ")
    DoB = input("Enter the students date of birth: ")
    return name, DoB
def append_to_lists(name, DoB):
    student.append(name)
    date_of_birth.append(DoB)
    return
def find_student(name):
    if name in student:
        return student.index(name)
    else:
        return 0
def print_birth(DoB):
    if i > 0:
        DoB = date_of_birth[i]
        print(DoB)
        year_of_birth = int(DoB[-2:])
        if year_of_birth >= 0 and year_of_birth <= 15:
            age = 15 - year_of_birth
        else:
            age = 2015 - year_of_birth - 1900
            print(year_of_birth)
            print(age)
    else:
        print("Student name not in list")
    return 
#main program
while count <= 5:
    name, DoB = student_details()
    append_to_lists(name, DoB)
    count = count + 1
name_to_find = input("Enter the name to find: ")
i = find_student(name_to_find)
age = print_birth
print_birth(DoB)




    
        
