import mysql.connector
import urllib2
import json
from urllib2 import Request   

try:
	from setuptools import setup

except ImportError: 
	from distutils.core import setup

config = {
	'description': 'Hangman Game in Python',
	'author': 'Quentin Au',
	'download_url': 'https://github.com/queeeentin/Hangman.git',
	'author_email': 'quentinubc@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['hangman'],
	'scripts': ['toolchan.sh'],
	'name': 'Hangma'
}

response = urllib2.urlopen("https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa-no-swears-medium.txt")
       #Gets an array of bytes!

wordList = []


for i in response.readlines():
	wordList.append(str(i).rstrip('\n'))

#setup (**config)
#Open database connection
db = mysql.connector.connect(user ="root", password = "8998", host = "127.0.0.1", database = "hangman" )


# prepare a cursor object using cursor() method
cursor = db.cursor()

for i in wordList:
	sql = """INSERT INTO SIMPLEWORDS (words) VALUE ('%s') """ % (i)
	cursor.execute(sql)
	db.commit()

cursor.close()
db.close()


