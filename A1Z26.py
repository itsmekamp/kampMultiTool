from itertools import cycle
import re

A1Zkey = {"a" : "1", "b" : "2", "c" : "3", "d" : "4", "e" : "5",
          "f": "6", "g": "7", "h": "8", "i": "9", "j": "10",
          "k": "11", "l": "12", "m": "13", "n": "14", "o": "15",
          "p": "16", "q": "17", "r": "18", "s": "19", "t": "20",
          "u": "21", "v": "22", "w": "23", "x": "24", "y": "25",
          "z" : "26"}
A1ZkeyInv = {v: k for k, v in A1Zkey.items()}

def encode(input):
    A1Zcycle = cycle(input)
    A1Znext = next(A1Zcycle)
    res = ""
    for char in input:
        if char in A1Zkey:
            A1Zthis, A1Znext = A1Znext, next(A1Zcycle)
            res += A1Zkey.get(char.lower())
            if A1Znext == " ":
                res += " "
            elif input.find(char) == len(input)-1:
                res += ""
            else:
                res += "-"
        else:
            res += char
    return res

def decode(input):
    result = ""
    newInput = []
    for i in input:
        newInput += list(filter(None, re.split("[-]", i)))
    print(newInput)
    for string in newInput:
        if string in A1ZkeyInv:
            result += A1ZkeyInv.get(string)
        elif string == " ":
            result += " "
        else:
            result += string
    return result
