#Harry Robinson
#01-01-2015
#Testing the capital of countries

import random

countrylist = ['Germany','United Kingdom','France','Spain','Austria','Italy','Nepal','Russia','Norway','Denmark']
citylist = ['Berlin','London','Paris','Madrid','Vienna','Rome','Kathmandu','Moscow','Oslo','Copenhagen']
def randomCountry():
    guessedIndex = random.randint(0, 9) 
    countryToGuess = countrylist[guessedIndex]
    answer = input("Enter the capital of {0}: ".format(countryToGuess))
    return answer, guessedIndex
def capitalVerification(answer, guessedIndex):
    correctCapital = citylist[guessedIndex]
    if correctCapital == answer:
        print("Capital correct")
    else:
        print("Capital is incorrect")
    return
#main program
answer, guessedIndex = randomCountry()
capitalVerification(answer, guessedIndex)
    
    
