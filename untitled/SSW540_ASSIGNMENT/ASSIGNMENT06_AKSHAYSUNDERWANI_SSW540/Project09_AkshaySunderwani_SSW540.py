# SSW 540 - Assignment 09 - P09: Classic Books
# Akshay Sunderwani

import operator
from string import punctuation
import os

def parsefileforpath(filepath):
    try:
        # opening the file
        if os.path.exists ( filepath ) and os.path.getsize ( filepath ) > 0:
            filehandler = open ( filepath , 'r' , encoding='utf-8' , errors='ignore')
            string_file = filehandler.read ( )

            main_dict = {}
            punc_translator = str.maketrans ( {key: None for key in punctuation} )
            cleanString = string_file.translate ( punc_translator ).lower().split()
            main_dict['Total_words'] = len(cleanString)


            wordsDict = {}
            for word in cleanString:
                wordsDict[ word ] = wordsDict.get ( word , 0 ) + 1
            main_dict['Distinct_words'] = len(wordsDict)


            wordList = []
            for key , value in wordsDict.items ( ):
                wordList.append ( (value , key) )
            wordList.sort ( reverse=True )
            main_dict['Top_25'] = wordList


            charDict = {}
            fileStr = ''.join ( cleanString )
            for i in range ( 0 , len ( fileStr ) ):
                char = fileStr[ i ]
                if str.isalpha ( char ):
                    charDict[ char ] = charDict.get ( char , 0 ) + 1
            charlist = []
            for key , value in charDict.items ( ):
                charlist.append ( (value , key) )
            charlist.sort ( reverse=True )
            main_dict['Char_count'] = charlist
            return main_dict
        else:
            return 'Either file not exists or the file is empty.'
    except EnvironmentError as error:
        return error


path = input ( "Please provide path for file to read : " )  # input path of file from user.
noofunique = parsefileforpath ( path )  # call parser method to read
if not isinstance(noofunique, dict):
    print('ERROR : ', noofunique)
else:
    if len(noofunique.keys()) > 0:
        if 'Total_words' in noofunique.keys():
            print('\nTotal no of words in file : ', noofunique['Total_words'])
        if 'Distinct_words' in noofunique.keys():
            print ( 'Total no of distinct word count : ' , noofunique['Distinct_words'] )
        if 'Top_25' in noofunique.keys():
            if len(noofunique['Top_25']) > 0:
                print ( '\nTop 25 words count :' )
                for value , key in noofunique[ 'Top_25' ][ :25 ]:
                    print ( key , value )
        if 'Char_count' in noofunique.keys():
            if len(noofunique['Char_count']) > 0:
                print ( "\nCharacter frequency in descending order: " )
                for value , key in noofunique['Char_count']:
                    print ( key , value )
