import os
import sys
import string

print ("*****Program to provide the summary of text file*****")


# function to get put file contents in dictionary
def getDictionary(fileContent):
    wordsDict = dict ( )
    for word in fileContent:
        wordsDict[ word ] = wordsDict.get ( word , 0 ) + 1
    return wordsDict


# function to get sorted dictionart based on the values
def getDictSortedWithValues(wordsDict):
    wordList = list ( )
    for key , value in wordsDict.items ( ):
        wordList.append ( (value , key) )
    wordList.sort ( reverse=True )
    return wordList


# function to calculate the total number of words in a file
def getCountofAllWords(fileContent):
    print("\nTotal number of words in file: " , len ( fileContent ))


# function to get number of distinct words in a file
def getCountofDistinctWords(fileContent):
    wordsDict = getDictionary ( fileContent )
    print("\nTotal number of distinct words in file: " , len ( wordsDict ))


def getTo25FrequentWords(fileContent):
    wordsDict = getDictionary ( fileContent )
    wordList = getDictSortedWithValues ( wordsDict )
    print("\nTop 25 most frequesnt words are: ")
    for value , key in wordList[ :25 ]:
        print(key , value)



# function to get the frequency of alphabets in the file. Not considering the numbers in characters
def getCharacterFrequency(fileContent):
    charDict = dict ( )
    fileStr = ''.join ( fileContent )
    for i in range ( 0 , len ( fileStr ) ):
        char = fileStr[ i ]
        if str.isalpha ( char ):
            charDict[ char ] = charDict.get ( char , 0 ) + 1
    charDict = getDictSortedWithValues ( charDict )
    print("\nCharacter frequency in descending order: ")
    for value , key in charDict:
        print(key , value)



# get the file name
# fileName = input ( "Enter the file name: " )
try:
    fHandle = open ( 'sample.txt' , 'r' )
    strFile = fHandle.read ( )
except IOError:
    print("Error: can\'t find file or read data")
    sys.exit ( )

if os.stat ( 'sample.txt' ).st_size != 0:  # to check if file is not empty
    fileContent = strFile.translate(string.punctuation).lower().split()
    # fileContent = strFile.translate ( None , string.punctuation ).lower ( ).split ( )
    getCountofAllWords ( fileContent )
    getCountofDistinctWords ( fileContent )
    getTo25FrequentWords ( fileContent )
    getCharacterFrequency ( fileContent )
else:
    print("Oops!!!This file is empty")
