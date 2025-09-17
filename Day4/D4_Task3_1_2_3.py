# 3.1
import string  # askip il y a .encode


def ceasar_cipher():
    message = str(input("What is your message?\n"))
    key = int(input("What is your key?\n"))
    encoded_message = ""
    ascii_letters = "abcdefghijklmnopqrstuvwxyz"  # est-ce que qqch existe déjà ??
    for letter in message.lower():
        if letter in ascii_letters:
            step = ascii_letters.find(letter) + key
            encoded_message += ascii_letters[step]
        else:
            encoded_message += letter
    print(encoded_message)


# ceasar_cipher()


# 3.2
def ceasar_cipher_decode_key(message, key):
    encoded_message = ""
    ascii_letters = "abcdefghijklmnopqrstuvwxyz"
    for letter in message.lower():
        if letter in ascii_letters:
            step = ascii_letters.find(letter) - key
            encoded_message += ascii_letters[step]
        else:
            encoded_message += letter
    print(encoded_message)


""" 
message = str(input("What is the message?\n"))
key = int(input("What is the key?\n"))
ceasar_cipher_decode_key((message,key))
 """


def ceasar_cipher_decode_no_key(message):
    encoded_message = []
    ascii_letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    for i in range(1, 26):
        encoded_message.append("")
        for letter in message.lower():
            if letter in ascii_letters:
                step = (ascii_letters.find(letter) + i) % 25
                encoded_message[-1] += ascii_letters[step]
            else:
                encoded_message += letter
        print(f"For key {i} your message is: {encoded_message[-1]}")


# message = str(input("What is the message?\n"))
# ceasar_cipher_decode_no_key(message)

# 3.3 + 3.4 ont leurs propres doc
