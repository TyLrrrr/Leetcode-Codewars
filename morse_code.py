#Codewars Challenge: translate morse code strings to english

def decode_morse(morse_code):
    alpha =" "
    morse_code = morse_code.replace("   ", "  ")
    x = morse_code.split(" ")
    for i in x:
        try:
            alpha += str(MORSE_CODE[i])
        except KeyError:
            alpha += " "
    return alpha.strip()
