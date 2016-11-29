# SSW 540 - Assignment 07 - P7: Finding unique strings
# Akshay Sunderwani

import re

def parsefileforpath(filepath):
    try:
        # opening the file
        with open ( filepath ) as filetoread:
            senderlist = [ ]
            for lines in filetoread:
                linelist = lines.split ( )
                if len ( linelist ) > 0:
                    # check for tag "From:" for getting email ids
                    if 'From:' in linelist[ 0 ]:
                        for items in linelist:
                            if linelist.index ( items ) != 0:
                                # used regex to identify valid email address and add it to the list if it is not in the
                                # list
                                if items not in senderlist and re.match (
                                        r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$" , items ):
                                    senderlist.append ( items )
            return len ( senderlist )
    except EnvironmentError as error:
        return error


path = input ( "Please provide path for file to read : " )  # input path of file from user.
noofunique = parsefileforpath ( path )  # call parser method to read
if isinstance(noofunique, FileNotFoundError):
    print('ERROR: ', noofunique)
else:
    print ( 'There are ' , noofunique , ' email address in the file.' )
