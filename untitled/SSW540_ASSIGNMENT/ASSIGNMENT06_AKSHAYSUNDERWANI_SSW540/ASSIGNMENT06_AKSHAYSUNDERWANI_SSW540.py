# SSW 540 - Assignment 06 - P6: Slicing & Dicing files
# Akshay Sunderwani


def parsefileforpath(filepath):
    try:
        # opening the file
        with open ( filepath ) as filetoread:
            total_lines = 0
            total_value = 0
            for lines in filetoread:
                linelist = lines.split ( )
                if len ( linelist ) > 0:
                    if 'X-DSPAM-Confidence' in linelist[0]:
                        try:
                            value = float ( linelist[ -1 ] )
                            total_lines += 1
                            total_value += value
                        except ValueError:
                            print ( 'Bad spam value!!!' )
            if total_lines > 0:
                try:
                    print ( 'Total spam lines : ' , total_lines ,
                            ' and average spam confidence : %.4f' % (total_value / total_lines) )
                except ZeroDivisionError as error:
                    print ( error )
            else:
                print ( 'Total spam lines : 0 and average spam count : 0' )
        print ( "File read complete, thank you for using this program." )
    except EnvironmentError as error:
        print ( error )


path = input ( "Please provide path for file to read : " )  # input path of file from user.
parsefileforpath ( path )  # call parser method to read
