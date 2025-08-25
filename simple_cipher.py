#A pyhton Cipher for Encyption and Decryption
#Shift by 3
def encrypt(text):
     alphabet = "abcdefghijklmnopqrstuvwxyz"
     result = ""
     for letter in text:
         if letter in alphabet:
             position = alphabet.index(letter)
             new_position = (position + 3) % 26
             result += alphabet[new_position]
         else:
             result += letter 
     return result
message = input ("Enter a message: ")
print("Encrypted:", encrypt(message))

