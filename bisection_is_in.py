#Czy litera znajduje sie w lancuchu znakow (metoda bisekcji)
from math import *

x = 'asdsada'

def isIn(char, aStr):
    aStr = ''.join(sorted(aStr))
    guess = int(floor(len(aStr)/2.0))
    print guess,' ',aStr,' ',aStr[guess],'\n'
    if aStr == '':
        return False
    elif len(aStr) == 1:
        if aStr == char:
            return True
        else:
            return False
    elif aStr[guess] == char:
        return True

    #head = 0
    #foot = -1
    if ord(aStr[guess])<ord(char):
        head = guess
        aStr = aStr[head:]
    else:
        foot = guess
        aStr = aStr[:foot]

    print '\n',aStr,'\n'
    return isIn(char,aStr)

x = 'abcde'
print isIn('a',x)
