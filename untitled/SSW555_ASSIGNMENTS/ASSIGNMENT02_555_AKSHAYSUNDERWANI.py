import os   # import to get path of directory where file is placed.
path = os.getcwd()  # method to fetch working directory path.

newpath = path + "/PROJECT00_FAMILYUPDATED_AKSHAYSUNDERWANI.ged"
# appending file name to working directory path. for testing
# newpath2 = "/Users/AKSHAY/PycharmProjects/untitled/PROJECT00_FAMILYUPDATED_AKSHAYSUNDERWANI.ged"


def parsefileforpath(filepath):

    basefilename = os.path.basename(filepath)
    basefilename2 = os.path.splitext(basefilename)

    # check if file is valid gedcom file.
    if basefilename2[-1] != '.ged':
        print("Please provide path for valid gedcom file to read.")
        return

    # list of valid tags
    validtags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV",
                 "DATE", "HEAD", "TRLR", "NOTE"]
    try:
        # opening the file
        with open(filepath) as filetoread:
            for lines in filetoread:
                linelist = lines.split()
                linelevel = linelist[0]
                if linelevel == '0':
                    lineid = linelist[1]
                    if lineid[0] == "@" and lineid[-1] == "@":
                        linetag = linelist[-1]
                    else:
                        linetag = linelist[1]
                else:
                    linetag = linelist[1]
                print("Line: ", lines[:-1])
                print("Level: ", linelevel)
                if linetag in validtags:
                    if linetag == 'DATE' and linelevel == '1':
                        linetaginfo = "Invalid"
                    else:
                        print("length of line list : ", linelist.__len__())
                        linelength = linelist.__len__() - 2
                        count = 2
                        linetaginfo = linetag
                        while linelength > 0:
                            linetaginf = " " + linelist[count]
                            count += 1
                            linelength -= 1
                            linetaginfo += linetaginf
                else:
                    linetaginfo = "Invalid"
                print("Tag info:", linetaginfo, '\n')
        print("File read complete, thank you for using this program.")
    except EnvironmentError as error:
        print(error)


path = input("Please provide path for file to read : ")     # input path of file from user.
parsefileforpath(path)  # call parser method to read
