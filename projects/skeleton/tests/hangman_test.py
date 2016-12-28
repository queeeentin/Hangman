from nose.tools import *
from hangman.hangman import *


#1.Nose supports fixtures, though we won't use them here. I have included the fixture methods in the below example, but only provide a comment explaining their use in the source.
#2.The nose.tools packages comes with many helper methods that make testing syntactically clearer for common test cases. In this example, we use assert_equal, assert_not_equal, 
#	the raises decorator, and assert_raises. For a full list see the nose.tools documentation.
#3.For organizational purposes, I create a subdirectory in my project called "tests". This is not required.


#Test functions may define setup and/or teardown attributes, 
#which will be run before and after the test function, respectively. 

def setup():
	"Set up test fixture, run before the test function" 
	hangman0 = Hangman('dictionary.txt')
	hangman1 = Hangman('testing-dic.txt')

	list1 = hangman0.creatListOfWords(hangman0.dicName)
	list2 = hangman1.creatListOfWords(hangman1.dicName)


def teardown():
	"tear down test fixture, run after the test function"
	print "TEAR DOWN!"


 #A convenient way to do this, especially when several test 
 #functions in the same module need the same setup, 
 #is to use the provided with_setup decorator:

@with_setup(setup,teardown)
def test_indexOfChar():
	hangman0 = Hangman('dictionary.txt')
	hangman1 = Hangman('testing-dic.txt')

	list1 = []
	list2 = ['h','e','l','l','o']
	list3 = ['b','e','c','a','u','s','e','e','e','e']
	list4 = [0,0,0,0,0,0,0]
	list5 = [None, None,None,None,None,None,None]
	list6 = [None,'a', 'b', None, 'c','a']

	indexList1 = []
	indexList2 = [2,3]
	indexList3 = [1,6,7,8,9]
	indexList4 = []
	indexList5 = []

 	assert_equal(indexList1,hangman0.indexOfChar('a',list1))
 	assert_equal(indexList2,hangman0.indexOfChar('l',list2))
 	assert_equal(indexList3,hangman0.indexOfChar('e',list3))
 	assert_equal(indexList4,hangman0.indexOfChar('b',list4))
 	assert_equal([0,1,2,3,4,5,6],hangman0.indexOfChar(0,list4))
 	assert_equal(indexList5,hangman0.indexOfChar('',list5))
 	assert_equal([0,1,2,3,4,5,6],hangman0.indexOfChar(None,list5))
 	assert_not_equal(indexList3,hangman0.indexOfChar('b',list4))
 	assert_not_equal(indexList2,hangman0.indexOfChar('b',list4))
 	assert_not_equal(indexList2,hangman0.indexOfChar('b',list4))

 	for index, i in enumerate(list6):
 		if i != 'a':
 			list6[index] = None

 	assert_is_none(list6[0])
 	assert_is_none(list6[2])
 	assert_is_not_none(list6[1])
 	assert_is_not_none(list6[5])



def test_randomWord():
	hangman0 = Hangman('dictionary.txt')
	hangman1 = Hangman('testing-dic.txt')

	list1 = hangman0.creatListOfWords(hangman0.dicName)
	list2 = hangman1.creatListOfWords(hangman1.dicName)
	dictionary = hangman0.dictionary
	
	word = hangman0.randomWord(dictionary)
	assert_in (word, list1)

	word1 = hangman1.randomWord(dictionary)
	assert_in(word1,list1)

	word2 = "where"
	word3 = "student" 
	word4 = 000

	assert_not_in(word3,dictionary)
	assert_not_in(word4,dictionary)
	assert_in (word2,dictionary)
	print "randomWord Test is don"

def test_win():
	hangman0 = Hangman('dictionary.txt')
	hangman1 = Hangman('testing-dic.txt')

	assert_false(hangman0.win)
	hangman0.win = True
	assert_true(hangman0.win)



