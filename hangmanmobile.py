import os
lives = 6
wordToGuess = raw_input("What word do you want them to guess?")
os.system("clear")
wordToGuessList = []
starredOutWord = []
print wordToGuess
for i in wordToGuess:
    wordToGuessList.append(i)
    starredOutWord.append("*")
print starredOutWord
print wordToGuessList
while ("*" in starredOutWord) and (lives != 0):
    os.system("clear")
    print "".join(starredOutWord)
    print "You have",lives,"lives remaining."
    guess = raw_input("What is your guess?")
    if guess in wordToGuessList:
        indices = [i for i, x in enumerate(wordToGuessList) if x == guess]
        for i in indices:
            starredOutWord[i] = guess   
    else:
        print "Wrong!"
        lives = lives -1
os.system("clear")
if lives == 0:
    print "You lose"
    print "The word was:",wordToGuess
else:
    print"You win, congratulations!"
