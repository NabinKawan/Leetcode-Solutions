class Solution(object):
    def decodeMessage(self, key, message):
        
        lowercase_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        encrypted = []
        
        for i in range(len(key)):
            if key[i] == " " or key[i] in encrypted:
                pass
            else:
                encrypted.append(key[i])
        

        result = ""
        

        for i in range(len(message)):
            if message[i] == " ":
                result += " "
            else:
                result += lowercase_alphabets[encrypted.index(message[i])]

        return result
