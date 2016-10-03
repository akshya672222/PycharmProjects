# SSW 540 - Assignment 05 - P5: String manipulation
# Akshay Sunderwani

# method to convert string to plural
def plurals(string):
    wordlist = string.split()   # get all the word(s) from the string
    vowelslist = ('ay', 'ey', 'iy', 'oy', 'uy', 'Ay', 'Ey', 'Iy', 'Oy', 'Uy', 'aY',
                  'eY', 'iY', 'oY', 'uY', 'AY', 'EY', 'IY', 'OY', 'UY')
    endswithylist = ('y', 'Y')
    endswithelselist = ('o', 'ch', 's', 'sh', 'x', 'z', 'O', 'CH', 'S', 'SH', 'X', 'Z', 'cH', 'Ch', 'sH', 'Sh')
    pluralstring = ''   # string to store the response
    for words in wordlist:
        if words.endswith(vowelslist):
            pluralstring += words + 's' + ' '
        elif words.endswith(endswithylist):
            pluralstring += words[:-1] + 'ies' + ' '
        elif words.endswith(endswithelselist):
            pluralstring += words + 'es' + ' '
        else:
            pluralstring += words + 's' + ' '

        if words == wordlist[-1]:
            pluralstring = pluralstring[:-1]
    return pluralstring #return the final response


def getuserstring():
    name = input('Hello and welcome! may I know your name : ')
    line = input('Hello! ' + name + ', please enter any statement or line : ')
    print('Prural of the line is : ', plurals(line))


getuserstring()
