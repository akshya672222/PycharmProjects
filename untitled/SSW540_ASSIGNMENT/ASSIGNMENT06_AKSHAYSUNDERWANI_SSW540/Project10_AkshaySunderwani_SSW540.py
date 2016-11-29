# SSW 540 - Assignment 10 - P10: Writing Regex's
# Akshay Sunderwani

import re


def parsefileforpath(filepath, search_string):
    try:
        with open ( filepath ) as filetoread:
            sum_of_revision = 0
            total_count = 0
            dict = {}
            for lines in filetoread:
                linelist = lines.split ( )
                if len ( linelist ) > 0:
                    regex = r"^"+search_string+"+:\s(\d+)$"
                    matches = re.findall ( regex , lines, flags=re.IGNORECASE )
                    if len(matches) > 0:
                        total_count += 1
                        sum_of_revision += int(matches[0])
            if total_count > 1:
                average = float(sum_of_revision/total_count)
            else:
                average = 0.0
            dict['total'] = total_count
            dict['average'] = average
            return dict
    except EnvironmentError as error:
        return error


path = input ( "Please provide path for file to read : " )  # input path of file from user.
dict_val = parsefileforpath ( path, 'New Revision' )  # call parser method to read
if not isinstance(dict_val, dict):
    print('ERROR : ', dict_val)
else:
    print('Average : %.1f' % dict_val['average'])
    print('Number of lines : ', dict_val['total'])
