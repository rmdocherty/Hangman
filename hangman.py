import random
lives = 6
words = open("words.txt").read().splitlines()
wordToGuess = random.choice(words)
wordToGuessList = []
starredOutWord = []
print wordToGuess
for i in wordToGuess:
    wordToGuessList.append(i)
    starredOutWord.append("*")
print starredOutWord
print wordToGuessList
while ("*" in starredOutWord) and (lives != 0):
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
if lives == 0:
    print "You lose"
    print "The word was:",wordToGuess
else:
    print"You win, congratulations!"
