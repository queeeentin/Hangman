import time, sys, os
import re, random
import webbrowser
from inputCheck import InputCheck
import mysql.connector


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

  def __init__(self):
    self.inputList=[]
    self.charList = []
    self.timeout = 5
    self.curHanman = 0
    self.numOfTry = 0
    self.win = False
    self.cwd  = os.path.dirname(os.path.realpath(__file__))


  def indexOfChar(self,char,chars):
    returnList = []
    for index, i in enumerate(chars):
      if char == i:
        returnList.append(index)

    return returnList


  def wongame(self,numOfTry,charList):
    print self.HANGMANPICS[numOfTry]
    for i in charList:
      print i,

    print "\n"
    print "Congratulation!!! You won the game!"
    webbrowser.open("file://" + self.cwd +"/win.gif")
    self.win = True

  def obtainWordsFromDataBase(self):
    list1 = []
    db = mysql.connector.connect(user ="root", password = "Qo6043608998!", host = "127.0.0.1", database = "hangman" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    sql = "SELECT words from SIMPLEWORDS ORDER BY RAND() LIMIT 1"
    cursor.execute(sql)
    for i in cursor:
      for j in i:
        list1.append(j)
    return list1[0]



  def main(self):
    inputList = self.inputList
    charList = self.charList
    timeout = self.timeout
    curHanman = self.curHanman
    numOfTry = self.numOfTry
    win = self.win

    word = ""
    

    if os.path.exists("wordList.txt"):
      fileObject = open("wordList.txt","r")
      data = fileObject.read()
      wordList = data.split(" ")
      word = wordList[random.randint(0,len(wordList))]
    else:
      word = self.obtainWordsFromDataBase()
      #Randomly pick a word form the database, then make a list of char in the word
      #and a matchedCharList with the size of the word

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
        self.wongame(numOfTry,charList)
        win = True
        break
      elif answer in charList or answer =="":
        indexesOfChar = self.indexOfChar(answer,charList)

        for j in indexesOfChar:
          marchedCharList[j] = answer

          if marchedCharList == charList:
            self.wongame(numOfTry,charList)
            win = True
            break
      elif answer not in charList:
        numOfTry += 1

    if numOfTry >= 6:
      print self.HANGMANPICS[len(self.HANGMANPICS)-1]
      print "Unfortunatly, you have lost the game.", 
      print "The correct answer is:", word
      webbrowser.open("file://" + self.cwd +"/death.gif")

    print "Type yes/no to try again or to exit"
    tryAgain = raw_input()

    if tryAgain in ["yes", "y"]:
      return 1
    elif tryAgain  in ["no", "n"]:
      return 0
      

nextGame = 1
while nextGame == 1:
  hangman0 = Hangman()
  nextGame = hangman0.main()


  









