import mysql.connector

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

#setup (**config)
#Open database connection
db = mysql.connector.connect(user ="root", password = "8998", host = "127.0.0.1", database = "hangman" )


# prepare a cursor object using cursor() method
cursor = db.cursor()

words = [ "verification","presence","envelope","example","science","newspaper","greeting", "puddle", "sound", "where", "take", "help", "does", "only", "through", "another", "little", "much", "work", "before", "large", "know", "line", "must", "place", "right", "big", "year", "teacher", "evening", "livingroom", "meaning", "schema", "methology", "oxygen", "because", "honour", "turtle", "general", "wireless", "therefore", "mostly", "teller", "whatever", "whenever", "boyfriend", "address", "afterward", "follow", "default", "information", "teriyaki", "menu", "ourselves", "warning", "reduce", "justify", "shower", "needle", "nasty", "altitude", "landscape", "classification", "surroudings", "differential", "sentence", "formation", "homesick", "thread", "disgusting", "smell", "motivation", "tremendous", "handicap", "picture", "against", "chance", "suitcase", "spelling", "airline", "spirit", "animal", "house", "point", "plagiarism", "letter", "mother", "answer", "found", "study", "still", "learn", "should", "america", "earchquake", "designer", "interview", "intervial", "interesting", "tsunami"]

for i in words:
	sql = """INSERT INTO SIMPLEWORDS (words) VALUE ('%s') """ % (i)
	cursor.execute(sql)
	db.commit()

cursor.close()
db.close()


