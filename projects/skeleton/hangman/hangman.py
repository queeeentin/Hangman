import time, sys
import re, random
from PIL import Image
import webbrowser
from inputCheck import InputCheck



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
    self.inputList=[]
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


  def wongame(self):
    print "Congratulation!!! You won the game!"
    webbrowser.open('file:///Users/zzxx/Desktop/hangman/projects/skeleton/hangman/win.gif')
    self.win = True


  def creatListOfWords(self,dicName):
    "Create and return a list of words from the dicName txt provided"
    returnList= []
    dictionaryObj = open(dicName,'r')
    
    for line in dictionaryObj:
      for word in line.split(" "):
        returnList.append(word)

    return returnList


  def main(self):
    inputList = self.inputList
    dictionary = self.dictionary
    charList = self.charList
    timeout = self.timeout
    curHanman = self.curHanman
    numOfTry = self.numOfTry
    win = self.win
    dicName = self.dicName

    #wonGameImage = Image.open('win.gif')

    dictionary =  self.creatListOfWords(dicName)
  
    #Randomly pick a word form the dictionary, then make a list of char in the word
    #and a matchedCharList with the size of the word
    word = self.randomWord(dictionary)
    #print word

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
      print inputList
      print "Please enter a letter to guess or what you think this word would be."
      
      answer = raw_input(">")
      

      inputCheck = InputCheck(answer)

      #Advanced User Input (exception handling)
      answer = inputCheck.input_scan(inputList)

      if answer == word:
        self.wongame()
        win = True
        break
      elif answer in charList or answer =="":
        indexesOfChar = self.indexOfChar(answer,charList)

        for j in indexesOfChar:
          marchedCharList[j] = answer

          if marchedCharList == charList:
            self.wongame()
            win = True
            break
      elif answer not in charList:
        numOfTry += 1

    if numOfTry >= 6:
      print self.HANGMANPICS[len(self.HANGMANPICS)-1]
      print "Unfortunatly, you have lost the game.", 
      print "The correct answer is:", word
      webbrowser.open("file:///Users/zzxx/Desktop/hangman/projects/skeleton/hangman/death.gif")

    print "Type yes/no to try again or to exit"
    tryAgain = raw_input()

    if tryAgain in ["yes", "y"]:
      return 1
    elif tryAgain  in ["no", "n"]:
      return 0
      

nextGame = 1
while nextGame == 1:
  hangman0 = Hangman('dictionary.txt')
  nextGame = hangman0.main()


  









