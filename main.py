# KampMultiTool
# by Kamp
# v1.0
# 2018

# If you are opening this file and saying the code is inefficient, yes it is probably
# I do not have a lot of experience in Python
# So dont expect anything great

#Import stuff

import math
import A1Z26
import CaesarCipher
import Fibonacci
import Atbash
import printHelp
from findInput import findInput
from findInput import findInputMath

print("Welcome to KampMultiTool!")
print("Enter help for Help!")
print("Enter your command:")
while True:
    choice = input("")
    #A1Z26
    if choice.startswith("a1z enc"):
        print(A1Z26.encode(findInput(choice, "a1z", "enc")))
    elif choice.startswith("a1z dec"):
        res = A1Z26.decode(findInput(choice, "a1z", "dec"))
        final = ""
        for char in res:
            if char == " ":
                final += " "
            else:
                final += char
        print(final)
    # Fibonacci
    elif choice.startswith("fib gen"):
        Fibonacci.generate(int(findInput(choice, "fib", "gen")))
    # Caesar Cipher
    elif choice.startswith("caesar enc"):
        print(CaesarCipher.encode(findInput(choice, "caesar", "enc")))
    elif choice.startswith("caesar dec"):
        print(CaesarCipher.decode(findInput(choice, "caesar", "dec")))
    # Atbash Cipher
    elif choice.startswith("atbash enc"):
        print(Atbash.encode(findInput(choice, "atbash", "enc")))
    elif choice.startswith("atbash dec"):
        print(Atbash.decode(findInput(choice, "atbash", "dec")))
    # Math
    elif choice.startswith("math add"):
        choice = findInputMath(choice, "math", "add")
        result = float(choice[0]) + float(choice[1])
        if result.is_integer():
            print(int(result))
        else:
            print(result)
    elif choice.startswith("math sub"):
        choice = findInputMath(choice, "math", "sub")
        result = float(choice[0]) - float(choice[1])
        if result.is_integer():
            print(int(result))
        else:
            print(result)
    elif choice.startswith("math mult"):
        choice = findInputMath(choice, "math", "mult")
        result = float(choice[0]) * float(choice[1])
        if result.is_integer():
            print(int(result))
        else:
            print(result)
    elif choice.startswith("math div"):
        choice = findInputMath(choice, "math", "div")
        result = float(choice[0]) / float(choice[1])
        if result.is_integer():
            print(int(result))
        else:
            print(result)
    elif choice.startswith("math mod"):
        choice = findInputMath(choice, "math", "mod")
        result = float(choice[0]) % float(choice[1])
        if result.is_integer():
            print(int(result))
        else:
            print(result)
    elif choice.startswith("math pow"):
        choice = findInputMath(choice, "math", "pow")
        result = float(choice[0]) ** float(choice[1])
        if result.is_integer():
            print(int(result))
        else:
            print(result)
    elif choice.startswith("math sqrt"):
        choice = findInputMath(choice, "math", "sqrt")
        result = math.sqrt(int(choice[0]))
        if result.is_integer():
            print(int(result))
        else:
            print(result)
    elif choice.startswith("math sq"):
        choice = findInputMath(choice, "math", "sq")
        result = int(choice[0]) ** 2
        print(result)
    elif choice.startswith("math areacf"):
        choice = findInputMath(choice, "math", "areacf")
        print(math.pi * int(choice[0]) * int(choice[0]))
    elif choice.startswith("math areac"):
        choice = findInputMath(choice, "math", "areac")
        print(round(math.pi * int(choice[0]) * int(choice[0]), 3))
    elif choice.startswith("math circumc r"):
        choice = findInputMath(choice, "math", "circumc", "r")
        print(round(math.pi * int(choice[0]) * int(choice[0]), 3))
    elif choice.startswith("math circumc d"):
        choice = findInputMath(choice, "math", "circumc", "d")
        print(round(math.pi * int(choice[0]), 3))
    elif choice.startswith("math rtod"):
        choice = findInputMath(choice, "math", "rtod")
        result = float(choice[0]) * 2
        if result.is_integer():
            print(int(result))
        else:
            print(result)
    elif choice.startswith("math dtor"):
        choice = findInputMath(choice, "math", "dtor")
        result = float(choice[0]) / 2
        if result.is_integer():
            print(int(result))
        else:
            print(result)
    # Help Command
    elif choice.startswith("help math"):
        printHelp.math()
    elif choice.startswith("help fib"):
        printHelp.fib()
    elif choice.startswith("help caesar"):
        printHelp.caesar()
    elif choice.startswith("help atbash"):
        printHelp.atbash()
    elif choice.startswith("help a1z"):
        printHelp.a1z26()
    elif choice.startswith("math"):
        printHelp.math()
    elif choice.startswith("fib"):
        printHelp.fib()
    elif choice.startswith("caesar"):
        printHelp.caesar()
    elif choice.startswith("atbash"):
        printHelp.atbash()
    elif choice.startswith("a1z"):
        printHelp.a1z26()
    elif choice.startswith("help"):
        printHelp.general()
    # Quit
    elif choice.startswith("q"):
        break
    else:
        print("Error : " + choice + " is not a defined command")
