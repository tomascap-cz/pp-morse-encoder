alphabet = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "k": ".---",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "'": ".----.",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    ":": "---...",
    ";": "-.-.-.",
    '"': ".-..-.",
    "_": "..--.-",
}

input_chars = list(input("Please type a word to be translated into Morse code: ").lower().replace(" ", ""))

morse_chars = [alphabet[char] for char in input_chars if char in alphabet.keys()]

if len(morse_chars) == len(input_chars):
    print(" | ".join(morse_chars))
else:
    print(f"The phrase includes invalid characters: {[char for char in input_chars if char not in alphabet.keys()]}")
