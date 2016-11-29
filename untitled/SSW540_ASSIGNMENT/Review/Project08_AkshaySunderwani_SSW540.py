# SSW 540 - Assignment 08 - P8: Counting unique items
# Akshay Sunderwani

import re


def parsefileforpath(filepath):
    try:
        # opening the file
        with open ( filepath ) as filetoread:
            maindict = {}
            noofemailrecevideddictionary = {}
            total_count = 0
            for lines in filetoread:
                linelist = lines.split ( )
                if len ( linelist ) > 0:
                    # check for tag "From:" for getting email ids
                    if 'From:' in linelist[ 0 ]:
                        for items in linelist:
                            if linelist.index ( items ) != 0:
                                # used regex to identify valid email address and add it to the dictionary and maintain
                                #  its count
                                if re.match (
                                        r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$" , items ):
                                    if items in noofemailrecevideddictionary:
                                        noofemailrecevideddictionary[items] += 1
                                    else:
                                        noofemailrecevideddictionary[items] = 1
                                    total_count += 1
            maindict['total_count'] = total_count
            maindict['email_info'] = noofemailrecevideddictionary
            return maindict
    except EnvironmentError as error:
        return error


path = input ( "Please provide path for file to read : " )  # input path of file from user.
noofunique = parsefileforpath ( path )  # call parser method to read
if not isinstance(noofunique, dict):
    print('ERROR : ', noofunique)
else:
    print('\nTotal no of email sent : ', noofunique['total_count'], '\nTotal by each email address :')
    print("\n".join("{}: {}".format(k, v) for k, v in noofunique['email_info'].items()))
    max_val = max(noofunique['email_info'].values())
    print('\nMax no of emails sent by :')
    for keys in noofunique['email_info']:
        if noofunique['email_info'][keys] == max_val:
            print(keys, ' : ', max_val, '\n')
