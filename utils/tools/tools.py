from .setting import *
def openTxt(name):
    with open(name,"r") as f:
        return f.read()

def addCoin(name,point=0):
    try:
        playerCoin = int(openTxt(name))
    except:
        playerCoin = 0
    playerCoin+=point
    with open(name,"w") as f:
            f.write(str(playerCoin))
    return playerCoin

def get_font(size): 
    return pygame.font.Font("8-BIT WONDER.TTF", size)

def listToString(s): 
    # initialize an empty string
    str1 = "" 
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 