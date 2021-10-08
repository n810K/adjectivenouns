import os
import random
from typing import final

print(os.getcwd())

nounWords = []
with open('wordlists/nouns.txt') as nounFile:
    for line in nounFile:
        nounWords.append(line.strip())

adjectiveWords = []
with open('wordlists/adjectives.txt') as adjectiveFile:
    for line in adjectiveFile:
        adjectiveWords.append(line.strip())

nounWordsLength = len(nounWords)
adjectiveWordsLength = len(adjectiveWords)

userAnswerNoun = ""
selectedNoun = " "
while (userAnswerNoun.lower() != "yes" and userAnswerNoun.lower() != "no"):
    userAnswerNoun = input("Would you like to enter your own noun? (yes/no) ")
    if (userAnswerNoun.lower() != "yes" and userAnswerNoun.lower() != "no"):
        print("Please enter yes/no")

if (userAnswerNoun.lower() == "yes"):
    while (not selectedNoun[0].isalpha()):
        selectedNoun = input("What would you like your noun to be? ")
        if (selectedNoun[0].isnumeric()):
            print("Please enter a valid noun")

else:
    selectedNoun = random.choice(nounWords)

# print(selectedNoun[0])
print("Your selected noun is:", selectedNoun)

userAnswerAdjective = ""
while (not userAnswerAdjective.isnumeric()):
    userAnswerAdjective = input("How many adjectives would you like to describe the noun? ")
    if (not userAnswerAdjective.isnumeric()):
        print("Please enter a valid number")



scopedAdjectiveList = []
for i in range(adjectiveWordsLength):
    if adjectiveWords[i][0] == selectedNoun[0].lower():
        scopedAdjectiveList.append(adjectiveWords[i])

scopedAdjectiveListLength = len(scopedAdjectiveList)

#print(scopedAdjectiveListLength)

if (int(userAnswerAdjective) > int(scopedAdjectiveListLength)):
    userAnswerAdjective = scopedAdjectiveListLength


randomIndex = random.sample(range(scopedAdjectiveListLength), int(userAnswerAdjective))

#print(scopedAdjectiveList)

finalAdjectiveList = []
for i in range(len(randomIndex)):
    finalAdjectiveList.append(scopedAdjectiveList[randomIndex[i]])

print(*finalAdjectiveList, selectedNoun)