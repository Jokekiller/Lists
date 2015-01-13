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
    while not done and index < len(unsorted_list):
        done = True
        for index in range((len(unsorted_list)-1)-1):
            if unsorted_list[index] > unsorted_list[index + 1]:
                done = False
                temp = unsorted_list[index]
                unsorted_list[index] = unsorted_list[index + 1]
                unsorted_list[index + 1] = temp
            else:
                done = True
        index = index + 1
    sorted_list = unsorted_list  
    return sorted_list
def test_bubble_sort():
    unsorted_list = ["Danish", "Andy", "John", "Toni", "Jack", "Indy"]
    sorted_list = bubble_sort(unsorted_list)
    print(sorted_list)
    return

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
people = ["Danish", "Andy", "Jack", "Indy", "John", "Toni"]
unsorted_list = people
done = bubble_sort(people)
sorted_list = test_bubble_sort()
print(sorted_list)
