import time, sys
import re, random
from PIL import Image

HANGMANPICS = ['''
 
    +---+
    |   |
        |
        |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']

#for i in HANGMANPICS:
#	print i
#	time.sleep (timeout)

def randomWord(words):
  randomIndex = random.randint(0,len(words)-1)
  returnWord = words[randomIndex]
  return returnWord

def indexOfChar(char,chars):
  returnList = []
  for index, i in enumerate(chars):
    if char == i:
      returnList.append(index)

  return returnList


def wongame(image):
  print "Congratulation!!! You won the game!"
  image.show()


def main():

  dictionary = []
  charList = []
  timeout = 5
  curHanman = 0
  numOfTry = 0
  win = False
  dictionaryObj = open('dictionary.txt','r')
  wonGameImage = Image.open('win.gif')

  #input the list of words from external txt file (dictionary.txt)
  for line in dictionaryObj:
    for word in line.split(" "):
      dictionary.append(word)
  print dictionary

  #Randomly pick a word form the dictionary, then make a list of char in the word
  #and a matchedCharList with the size of the word
  word = randomWord(dictionary)
  print word

  marchedCharList = [None] * len(word)
 
  for i in word:
    charList.append(i)
    print charList


  while numOfTry < 6 and win != True:
    print HANGMANPICS[numOfTry]
    
    for i in marchedCharList:
      if i != None:
        print i,
      else:
        print "__",

    print "\n"
    print "Please enter a letter to guess or what you think this word would be."
    answer = raw_input()
    if answer == word:
      win = True
      wongame(wonGameImage)
    elif answer in charList:
      indexesOfChar = indexOfChar(answer,charList)
      print indexesOfChar
      
      for j in indexesOfChar:
        marchedCharList[j] = answer
        print marchedCharList

      if marchedCharList == charList:
        wongame(wonGameImage)

    elif answer not in charList:
      numOfTry += 1




  #Failed condition: print "You Lost" print dead man
  if numOfTry >= 6:
    print HANGMANPICS[len(HANGMANPICS)-1]
    print "You Lost"

  print "Type yes/no to try again or to exit"
  tryAgain = raw_input()

  if tryAgain == "yes":
    main()
  else:
    sys.exit(0)


main()

  









