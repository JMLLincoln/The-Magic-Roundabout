import json
import random

with open("wordsPos.json", 'r') as f:
    jsonString = f.read()
    wordPositions = json.loads(jsonString)
    
def encode(word):
    message = []
    l = int(len(word) / 2)

    for letter in word:
        possibleWords = wordPositions[letter.lower()]["%s" % l]
        r = random.randint(1, len(possibleWords))
        p = possibleWords[r]

        with open("words.txt", 'r') as f:
            for i, line in enumerate(f):
                if i == p:
                    message.append(line.replace("\n", ""))

    return " ".join(message)

def decode(string):
    maxi = 1000
    string = string.split(" ")
    
    for word in string:
        if len(word) < maxi:
            maxi = len(word)

    counter = 0
    newString = []
    while counter < maxi:
        newWord = ""
        for word in string:
            newWord += word[counter]

        newString.append(newWord.lower())
        
        counter += 1
        
    return newString

running = True

while running:
    string = input("Input >: ")
    string = string.split(" ")

    encodedWords = []
    for word in string:
        encodedWords.append(encode(word))

    if len(encodedWords) == 1:
        print ("Encoded message: ")
        print (encodedWords[0])
        print ("\nPossible decoded messages: ")
        for item in decode(encodedWords[0]):
            print(item)
    else:
        print ("Encoded message: ")
        print(" ".join(encodedWords))
        print ("\nPossible decoded messages: ")
        for item in decode(" ".join(encodedWords)):
            print(item)
