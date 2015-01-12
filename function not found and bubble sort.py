#Harry Robinson
#12-01-2015
#function for found

def linear_search(searchList, searchItem):
    found = False
    index = 0
    while not found and index < len(people):
        if search_person == people[index]:
            found = True
        else:
            index = index + 1
    return found
def bubble_sort(unsorted_list):
    done = False
    index = 0
    while not done and index < len(people):        
        temp = people[index]
        people[index] = people[index + 1]
        people[index] = temp
        people = people[index + 1]
        done = True
    return sorted_list

#main program
people = ["Danish", "Andy", "Jack", "Indy", "John", "Toni"]
search_person = input("Enter a name: ")
searchItem = people
searchList = search_person
found = linear_search(searchList, searchItem)
if found == True:
    print("Found")
else:
    print("Not found")
unsorted_list = people
done = bubble_sort(unsorted_list)
