CaesarKey = {"a" : "d", "b" : "e", "c" : "f", "d" : "g", "e" : "h",
             "f": "i", "g": "j", "h": "k", "i": "l", "j": "m",
             "k": "n", "l": "o", "m": "p", "n": "q", "o": "r",
             "p": "s", "q": "t", "r": "u", "s": "v", "t": "w",
             "u": "x", "v": "y", "w": "z", "x": "a", "y": "b",
             "z" : "c", "A" : "D", "B" : "E", "C" : "F", "D" : "G", "E" : "H",
             "F": "I", "G": "J", "H": "K", "I": "L", "J": "M",
             "K": "N", "L": "O", "M": "P", "N": "Q", "O": "R",
             "P": "S", "Q": "T", "E": "U", "S": "V", "T": "W",
             "U": "X", "V": "Y", "W": "Z", "X": "A", "Y": "B",
             "Z" : "C"}
CaesarKeyInv = {v: k for k, v in CaesarKey.items()}

# Caesar Cipher Encoding Function
def encode(input):
    return "".join(CaesarKey.get(character) or character for character in input)

# Caesar Cipher Decoding Function
def decode(input):
    return "".join(CaesarKeyInv.get(character) or character for character in input)
