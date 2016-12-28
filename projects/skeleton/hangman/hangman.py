import time, sys
import re, random
from PIL import Image


class Hangman (object):

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

  def __init__(self,dicName):
    self.dictionary = self.creatListOfWords(dicName)
    self.charList = []
    self.timeout = 5
    self.curHanman = 0
    self.numOfTry = 0
    self.win = False
    self.dicName = dicName
    

  def randomWord(self,words):
    randomIndex = random.randint(0,len(words)-1)
    returnWord = words[randomIndex]
    return returnWord



  def indexOfChar(self,char,chars):
    returnList = []
    for index, i in enumerate(chars):
      if char == i:
        returnList.append(index)

    return returnList


  def wongame(self,image):
    print "Congratulation!!! You won the game!"
    image.show()
    won = True


  def creatListOfWords(self,dicName):
    "Create and return a list of words from the dicName txt provided"
    returnList= []
    dictionaryObj = open(dicName,'r')
    
    for line in dictionaryObj:
      for word in line.split(" "):
        returnList.append(word)

    return returnList


  def main(self):

    dictionary = self.dictionary
    charList = self.charList
    timeout = self.timeout
    curHanman = self.curHanman
    numOfTry = self.numOfTry
    win = self.win
    dicName = self.dicName

    wonGameImage = Image.open('win.gif')

   
    dictionary =  self.creatListOfWords(dicName)
  
    #Randomly pick a word form the dictionary, then make a list of char in the word
    #and a matchedCharList with the size of the word
    word = self.randomWord(dictionary)
    print word

    marchedCharList = [None] * len(word)
   
    for i in word:
      charList.append(i)


    while numOfTry < 6 and win != True:
      print self.HANGMANPICS[numOfTry]
      
      for i in marchedCharList:
        if i != None:
          print i,
        else:
          print "__",

      print "\n"
      print "Please enter a letter to guess or what you think this word would be."
      answer = raw_input()
      if answer == word:
        self.wongame(wonGameImage)
        break
      elif answer in charList:
        indexesOfChar = self.indexOfChar(answer,charList)
        
        for j in indexesOfChar:
          marchedCharList[j] = answer

        if marchedCharList == charList:
          self.wongame(wonGameImage)
          break

      elif answer not in charList:
        numOfTry += 1

    if numOfTry >= 6:
      print self.HANGMANPICS[len(self.HANGMANPICS)-1]
      print "You Lost"

    print "Type yes/no to try again or to exit"
    tryAgain = raw_input()

    if tryAgain == "yes":
      return 1
    else:
      return 0
      

nextGame = 1
while nextGame == 1:
  hangman0 = Hangman('dictionary.txt')
  nextGame = hangman0.main()


  









