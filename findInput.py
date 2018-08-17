def findInput(input, string1="", string2="", string3="", string4="", string5=""):
    input = input.split(" ")
    if not string1 == "":
        input.remove(string1)
    if not string2 == "":
        input.remove(string2)
    if not string3 == "":
        input.remove(string3)
    if not string4 == "":
        input.remove(string4)
    if not string5 == "":
        input.remove(string5)
    input = " ".join(input)
    return input
def findInputMath(input, string1="", string2="", string3="", string4="", string5=""):
    input = input.split(" ")
    if not string1 == "":
        input.remove(string1)
    if not string2 == "":
        input.remove(string2)
    if not string3 == "":
        input.remove(string3)
    if not string4 == "":
        input.remove(string4)
    if not string5 == "":
        input.remove(string5)
    input = list(map(float, input))
    return input