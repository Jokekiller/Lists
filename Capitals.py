#Harry Robinson
#01-01-2015
#Testing the capital of countries

import random

correct = 0

def randomCountry():
    guessedIndex = random.randint(0, 9) 
    countryToGuess = countrylist[guessedIndex]
    answer = input("Enter the capital of {0}: ".format(countryToGuess))
    return answer, guessedIndex
def capitalVerification(answer, guessedIndex):
    global correct
    correctCapital = citylist[guessedIndex]
    if correctCapital == answer:
        print("Capital correct")
        correct = correct + 1 
    else:
        print("Capital is incorrect")
    return
#main program
count = 1
while count <= 5:
    countrylist = ['Germany','United Kingdom','France','Spain','Austria','Italy','Nepal','Russia','Norway','Denmark']
    citylist = ['Berlin','London','Paris','Madrid','Vienna','Rome','Kathmandu','Moscow','Oslo','Copenhagen']
    answer, guessedIndex = randomCountry()
    capitalVerification(answer, guessedIndex)
    count = count + 1
print("Total score is {0}/5.".format(correct))

    
    
