class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.alph_to_num  = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7, "i" : 8,
                        "j" : 9,"k" : 10,"l" : 11,"m" : 12,"n" : 13, "o" : 14,"p" : 15, "q" : 16,"r" : 17,
                        "s" : 18,"t" : 19, "u" : 20,"v" : 21,"w" : 22,"x" : 23,"y" : 24, "z" : 25}
        self.num_key= []
        for char in self.key:
            if char in self.alph_to_num:
                self.num_key.append(self.alph_to_num[char])
        pass
    
    def encode(self, text):
        alphabet = self.alphabet
        num_key = self.num_key
        encoded = ""
        capital = ""
        counter = 0
        x = 0
        if len(num_key) < len(text):
            num_key = num_key * 5
            
                
        for i in text:
            try:
                x = alphabet.index(i)
            except Exception:
                capital += i
            y = x + num_key[counter]
            if y > 25:
                x = 26 - x
                y = num_key[counter] - x
                encoded += alphabet[y]
            else:
                encoded += alphabet[y]
            counter += 1
        print(encoded)
        if len(capital) > 0:
            return capital
        else:
            return encoded
    
    def decode(self, text):
        alphabet = self.alphabet
        num_key = self.num_key
        decoded = ""
        capital = ""
        counter = 0
        x = 0
        if len(num_key) < len(text):
            num_key = num_key * 5
        

        for i in text:
            try:
                x = alphabet.index(i)
            except Exception:
                capital += i
            y = x - num_key[counter]
            if y < 0:
                y = 26 + y
                decoded += alphabet[y]
            else:
                decoded += alphabet[y]
            counter += 1
        print(decoded)
        if len(capital) > 0:
            return capital
        else:
            return decoded
