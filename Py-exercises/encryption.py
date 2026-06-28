import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

plain_text = input("Enter a text to encrypt: ")
encrypted_txt = ""

for letter in plain_text:
    index = chars.index(letter)
    encrypted_txt += key[index]

print(f"Plain text: {plain_text}")
print(f"Encrypted text: {encrypted_txt}")