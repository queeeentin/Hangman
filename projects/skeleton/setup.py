try:
	from setuptools import setup

except ImportError: 
	from distutils.core import setup

config = [
	'description': 'Hangman Game in Python',
	'author': 'Quentin Au',
	'download_url': 'https://github.com/queeeentin/Hangman.git',
	'author_email': 'quentinubc@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['hangman'],
	'scripts': ['toolchan.sh'],
	'name': 'Hangma'
]

setup (**config)
