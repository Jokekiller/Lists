#Harry Robinson
#17-01-2015
#Random numbers list

import random

def adding_to_list():
    numberList = []
    for index in range(0,19):
        numberList.append(index)
    return numberList
def generating_number(numberList):
    number = 0
    while number < 6:
        index = random.randint(1,19)
        value = numberList[index]
        if value > 0:
            number = number + 1
            print(value)
            numberList.insert(index, 0)
    return

#main program
numberList = adding_to_list()
generating_number(numberList)
print(numberList)       
    
    
