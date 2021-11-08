import math
import os
import pyperclip as pc

sRamStr = pc.paste()
total = math.ceil(len(sRamStr)/100)
lineName = ""
def init():
    printName()
    global lineName
    lineName = input("Input Line Name: ")
    os.system('cls')
    printMenu()
    

def printName():
    print(r"""
_________/\\\___/\\\\\\\\\\\\\___________________________________________________        
 ________\/\\\__\/\\\/////////\\\_________________________________________________       
  ________\/\\\__\/\\\_______\/\\\________________/\\\___________________/\\\______      
   ________\/\\\__\/\\\\\\\\\\\\\/___/\\/\\\\\\\__\///___/\\/\\\\\\____/\\\\\\\\\\\_     
    ___/\\\\\\\\\__\/\\\/////////____\/\\\/////\\\__/\\\_\/\\\////\\\__\////\\\////__    
     __/\\\////\\\__\/\\\_____________\/\\\___\///__\/\\\_\/\\\__\//\\\____\/\\\______   
      _\/\\\__\/\\\__\/\\\_____________\/\\\_________\/\\\_\/\\\___\/\\\____\/\\\_/\\__  
       _\//\\\\\\\\\__\/\\\_____________\/\\\_________\/\\\_\/\\\___\/\\\____\//\\\\\___ 
        __\/////////___\///______________\///__________\///__\///____\///______\/////____
""")

def printMenu():
    printName()
    print("""\
                      [1]        Write String To Flash          [1]
                      [2]          Print Statements             [2]
                      [3]       Copy From Clipboard Again       [3]
                      [4]           Set New Line Name           [4]""")

    switch = input()
    os.system('cls')
    
    if switch == "1":
        sram2flash()
    elif switch == "2":
        prStatement()
    elif switch == "3":
        cpyClip()
    elif switch == "4":
        init()
    else:
        printMenu()

    printMenu()

def cpyClip():
    global sRamStr
    global total
    sRamStr = pc.paste()
    total = math.ceil(len(sRamStr)/100)

def sram2flash():
    lines = []
    loop = 0
    for y in range(total):
        lines.append("")
        for i in range(100):
            lines[y] += (sRamStr[loop])
            loop += 1
            if (loop == len(sRamStr)):
                break

    finaltext = ""
    for x in range(total):
        if (x == 0):
            finaltext += ("const char " + lineName + str(x) + "[] PROGMEM = \"" + lines[x] + "\";")
        else:
            finaltext += ("\nconst char " + lineName + str(x) + "[] PROGMEM = \"" + lines[x] + "\";")
    
    pc.copy(finaltext)

def prStatement():
    finaltext = ""
    for x in range(total):
        if (x == 0):
            finaltext += ("DigiKeyboard.dPrint(" + lineName + str(x) + ");")
        else:
            finaltext += ("\nDigiKeyboard.dPrint(" + lineName + str(x) + ");")
    
    pc.copy(finaltext)

init()