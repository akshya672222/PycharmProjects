from datetime import datetime
import operator


# method to handle the dictionary of siblings to fetch the difference between their birthdates
def days_between(dictofdate, familyid):
    length = len(dictofdate)
    response = ''
    if length > 15:
        response += '\nERROR: THERE ARE MORE THAN 15 SIBLINGS IN ' + familyid + ' FAMILY.'
    else:
        response += '\nINFO: THERE ARE ' + repr ( length ) + ' SIBLINGS IN ' + familyid + ' FAMILY.'
    newdict = {}
    for keys in dictofdate:
        if isinstance(dictofdate[keys], dict):
            newdict[keys] = dictofdate[keys]['VAL']
    sorted_list = sorted(newdict.items(), key=operator.itemgetter(1))
    i = 0
    while i < len(sorted_list)-1:
        j = i + 1
        while j < len(sorted_list):
            d1 = newdict[sorted_list[i][0]]
            d2 = newdict[sorted_list[j][0]]
            date1 = datetime.strptime ( d1.strftime('%m/%d/%Y') , "%m/%d/%Y" )
            date2 = datetime.strptime ( d2.strftime('%m/%d/%Y') , "%m/%d/%Y" )
            numberofdays = int(abs((date1 - date2).days))
            if (2 > numberofdays >= 0) or numberofdays > 243:
                response += '\nINFO: DATE OF BIRTH OF ' + sorted_list[i][0] + ' AND ' + sorted_list[j][0] + ' HAVE NO ERROR.'
                i += 1
                break
            else:
                response += '\nERROR: THERE IS UNUSUAL DIFFERENCE IN DATE OF BIRTH OF ' + keys[i] + ' AND ' + keys[j] +'.'
                j += 1
    return response


# method to get list of unique husband and wife ids from all families
def gethusbandandwifedict(dict):
    husbwifedict = {}
    husblist = []
    wifelist = []
    for key in sorted ( dict[ 'FAM' ] , key=lambda x: int ( x.replace ( '@' , "" ).replace ( 'F' , "" ) ) ):
        if 'HUSB' in dict['FAM'][key]:
            if dict['FAM'][key]['HUSB']['VAL'] not in husblist:
                husblist.append(dict['FAM'][key]['HUSB']['VAL'])
        if 'WIFE' in dict['FAM'][key]:
            if dict['FAM'][key]['WIFE']['VAL'] not in wifelist:
                wifelist.append(dict['FAM'][key]['WIFE']['VAL'])

    husbwifedict['HUSB'] = husblist
    husbwifedict['WIFE'] = wifelist
    return husbwifedict


# method to parse the main dictionary and generate response for user stories
def getsiblingsbdate(dict):
    # LOOP ACCORDING TO FAMILY
    siblingdict = {}
    response = ''
    famid = ''
    for key in sorted ( dict[ 'FAM' ] , key=lambda x: int ( x.replace ( '@' , "" ).replace ( 'F' , "" ) ) ):
        if siblingdict.__len__() > 0:
            response += days_between ( siblingdict , famid)
        siblingdict = {}
        if 'CHIL' in dict[ 'FAM' ][ key ]:
            if type ( dict[ 'FAM' ][ key ][ 'CHIL' ] ) is list:
                for d in dict[ 'FAM' ][ key ][ 'CHIL' ]:
                    famid = key
                    if 'BIRT' in dict[ 'INDI' ][ d[ 'VAL' ] ]:
                        if 'DATE' in dict[ 'INDI' ][ d[ 'VAL' ] ][ 'BIRT' ]:
                            siblingdict.update({d['VAL'] : {'VAL' : dict['INDI'][d['VAL']]['BIRT']['DATE']['VAL']}})
                        else:
                            siblingdict.update({d['VAL'] : 'N/A'})
                    else:
                        siblingdict.update ( {d[ 'VAL' ]: 'N/A'} )
            else:
                if 'BIRT' in dict[ 'INDI' ][ dict[ 'FAM' ][ key ][ 'CHIL' ][ 'VAL' ] ]:
                    if 'DATE' in dict[ 'INDI' ][ dict[ 'FAM' ][ key ][ 'CHIL' ][ 'VAL' ] ][ 'BIRT' ]:
                        response += '\nINFO: THERE IS ONLY 1 SIBLING IN THE FAMILY ' + key + ' : ' +\
                                            dict[ 'FAM' ][ key ][ 'CHIL' ][ 'VAL' ]\
                                            + ' AND ITS BIRTHDATE : ' +\
                                            dict[ 'INDI' ][ dict[ 'FAM' ][ key ][ 'CHIL' ][ 'VAL' ] ][ 'BIRT' ][ 'DATE' ][ 'VAL' ].strftime('%m/%d/%Y')
                    else:
                        response += '\nWARNING: THERE IS ONLY 1 SIBLING IN THE FAMILY ' + key + ' : ' +\
                                            dict[ 'FAM' ][ key ][ 'CHIL' ][ 'VAL' ]\
                                            + ' AND ITS BIRTHDATE IS NOT AVAILABLE.'
                else:
                    response += '\nWARNING: THERE IS ONLY 1 SIBLING IN THE FAMILY ' + key + ' : ' + \
                                        dict[ 'FAM' ][ key ][ 'CHIL' ][ 'VAL' ] \
                                        + ' AND ITS BIRTHDATE IS NOT AVAILABLE.'
        else:
            response += '\nINFO: NO CHILDREN AVAILABLE IN FAMILY ' + key + '.'
    return response


# method to check if response dictionary is valid or not
def run(out):
    ressponse = getsiblingsbdate(out)
    # print('response : ', ressponse)
    return ressponse
