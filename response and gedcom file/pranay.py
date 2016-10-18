from datetime import datetime


# check if date is in future
def checkifdateisinfuture(type, date, id):
    if date > datetime.now():
        return '\nERROR: ' + type + ' DATE OF ' + id + ' IS IN FUTURE.'
    else:
        return '\nINFO: ' + type + ' DATE OF ' + id + ' IS ' + date.strftime("%B %d, %Y")


# method to get list of unique husband and wife ids from all families
def gethusbandandwifedict(dict):
    husblist = [ ]
    wifelist = [ ]
    response = ''
    for key in sorted ( dict[ 'FAM' ] , key=lambda x: int ( x.replace ( '@' , "" ).replace ( 'F' , "" ) ) ):
        if 'HUSB' in dict[ 'FAM' ][ key ]:
            if dict[ 'FAM' ][ key ][ 'HUSB' ][ 'VAL' ] not in husblist:
                husblist.append ( dict[ 'FAM' ][ key ][ 'HUSB' ][ 'VAL' ] )
                if 'SEX' in dict['INDI'][dict['FAM'][key]['HUSB']['VAL']]:
                    if dict['INDI'][dict['FAM'][key]['HUSB']['VAL']]['SEX']['VAL'] != 'M':
                        response += '\nERROR: HUSBAND ' + dict['FAM'][key]['HUSB']['VAL'] + ' IN FAMILY ' + key + ' IS NOT MALE.'
                    else:
                        response += '\nINFO: HUSBAND ' + dict['FAM'][key]['HUSB']['VAL'] + ' IN FAMILY ' + key + ' IS MALE.'
        if 'WIFE' in dict[ 'FAM' ][ key ]:
            if dict[ 'FAM' ][ key ][ 'WIFE' ][ 'VAL' ] not in wifelist:
                wifelist.append ( dict[ 'FAM' ][ key ][ 'WIFE' ][ 'VAL' ] )
                if 'SEX' in dict['INDI'][dict['FAM'][key]['WIFE']['VAL']]:
                    if dict['INDI'][dict['FAM'][key]['WIFE']['VAL']]['SEX']['VAL'] != 'F':
                        response += '\nERROR: WIFE ' + dict['FAM'][key]['WIFE']['VAL'] + ' IN FAMILY ' + key + ' IS NOT FEMALE.'
                    else:
                        response += '\nINFO: WIFE ' + dict['FAM'][key]['WIFE']['VAL'] + ' IN FAMILY ' + key + ' IS FEMALE.'
    return response


# method to acess the dictionary and check for birth, death, marriage and divorce date
def datesbeforecurrentdate(maindict):
    response = '\n\n\n\n'
    # loop for individual birth and death date check
    for key in sorted ( maindict[ 'INDI' ] , key=lambda x: int ( x.replace ( '@' , "" ).replace ( 'I' , "" ) ) ):
        if 'BIRT' in maindict[ 'INDI' ][ key ]:
            if 'DATE' in maindict[ 'INDI' ][ key ][ 'BIRT' ]:
                response += checkifdateisinfuture('BIRTH', maindict['INDI'][key]['BIRT']['DATE']['VAL'], key)
            else:
                response += '\nWARNING: BIRTH DATE FOR ' + key + ' IS NOT AVAILABLE.'
        else:
            response += '\nWARNING: BIRTH DATE FOR ' + key + ' IS NOT AVAILABLE.'
        if 'DEAT' in maindict[ 'INDI' ][ key ]:
            if maindict[ 'INDI' ][ key ][ 'DEAT' ][ 'VAL' ] == 'Y':
                if 'DATE' in maindict[ 'INDI' ][ key ][ 'DEAT' ]:
                    response += checkifdateisinfuture('DEATH', maindict['INDI'][key]['DEAT']['DATE']['VAL'], key)
                else:
                    response += '\nWARNING: DEATH DATE FOR ' + key + ' IS NOT AVAILABLE.'
            else:
                response += '\nINFO: PERSON ' + key + ' IS ALIVE.'
        else:
            response += '\nINFO: PERSON ' + key + ' IS ALIVE.'

    # loop for family marriage and divorce date check
    for key in sorted ( maindict[ 'FAM' ] , key=lambda x: int ( x.replace ( '@' , "" ).replace ( 'F' , "" ) ) ):
        if 'MARR' in maindict[ 'FAM' ][ key ]:
            if 'DATE' in maindict['FAM'][key]['MARR']:
                response += checkifdateisinfuture('MARRIAGE', maindict['FAM'][key]['MARR']['DATE']['VAL'], key)
            else:
                response += '\nWARNING: MARRIAGE DATE OF ' + key + ' IS NOT AVAILABLE.'
        else:
            response += '\nWARNING: MARRIAGE DATE OF ' + key + ' IS NOT AVAILABLE.'
        if 'DIV' in maindict[ 'FAM' ][ key ]:
            if 'DATE' in maindict['FAM'][key]['DIV']:
                response += checkifdateisinfuture('DIVORCE', maindict['FAM'][key]['DIV']['DATE']['VAL'], key)
            else:
                response += '\nWARNING: DIVORCE DATE OF ' + key + ' IS NOT AVAILABLE.'

    response += gethusbandandwifedict(maindict)
    return response


def run(out):
    response = datesbeforecurrentdate(out)
    return response
