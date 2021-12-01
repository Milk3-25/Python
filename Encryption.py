#Making a encryption service
import os
import math

def clear():
    os.system('cls')

def processU(letter):
    return str((letter ** 2) * 4 + 24) + "U"

def processT(letter):
    return str((letter ** 2) * 3 - 6) + "T"

def processP(letter):
    return str((letter ** 2) * 5 + 56) + "P"

def process_(letter):
    return str((letter ** 2) * 2 - 89) + "O"

def processL(letter):
    return str((letter ** 2) * 4 + 4) + "L"

def encryption_portal():
    print("Enter desired text here\n>>", end = " ")
    To_Encrypt = str(input())
    encryptedText = ""
    for i in To_Encrypt:
        o = ord(i)
        y = 0
        if o >= 32 and o <= 64:
            y = str(processU(o))
        elif o >= 65 and o <= 90:
            y = str(processT(o))
        elif o >= 91 and o <= 96:
            y = str(processP(o))
        elif o >= 97 and o <= 122:
            y = str(process_(o))
        elif o >= 123 and o <= 126:
            y = str(processL(o))
        encryptedText += y
    print(encryptedText)



def rprocessU(letter):
    con = int(math.sqrt((letter - 24) / 4))
    return chr(con)

def rprocessT(letter):
    con = int(math.sqrt((letter + 6) / 3))
    return chr(con)

def rprocessP(letter):
    con = int(math.sqrt((letter - 56) / 5))
    return chr(con)

def rprocess_(letter):
    con = int(math.sqrt((letter + 89) / 2))
    return chr(con)

def rprocessL(letter):
    con = int(math.sqrt((letter - 4) / 4))
    return chr(con)

'''
Input: none
Output: Decrypted string
Acts as a retriver of all the different decription processes and returns the decrypted string
'''
def decryption_portal():
    print("Enter desired text here\n>>", end = " ")
    To_Decrypt = str(input())
    decryptedText = ""
    start = 0
    for i in range(len(To_Decrypt)):
        o = To_Decrypt[i]
        y = ""
        if o == "U":
            y = rprocessU(float(To_Decrypt[start:i]))
            start += len(To_Decrypt[start:i]) + 1
        elif o == "T":
            y = rprocessT(float(To_Decrypt[start:i]))
            start += len(To_Decrypt[start:i]) + 1
        elif o == "P":
            y = rprocessP(float(To_Decrypt[start:i]))
            start += len(To_Decrypt[start:i]) + 1
        elif o == "O":
            y = rprocess_(float(To_Decrypt[start:i]))
            start += len(To_Decrypt[start:i]) + 1
        elif o == "L":
            y = rprocesL(float(To_Decrypt[start:i]))
            start += len(To_Decrypt[start:i]) + 1
        decryptedText += y
    print(decryptedText)

# The main body iteration through the program until terminated by user
while(True):
    print("Welcome to encryption corp.\nPlease enter desired action.\nA) Encrypt\nB) Decrypt\nC) Exit")
    u = input()
    if (u.upper() == "A" or u.upper() == "ENCRYPT"):
        encryption_portal()
            
    elif (u.upper() == "B" or u.upper() == "DECRYPTION"):
        decryption_portal()
        
    elif (u.upper() == "EXIT" or u.upper() == "C"):
        print("Bye")
        quit()
        
    else:
        clear()
        print("Enter a valid command")
