### On suppose pour les deux fontions que les clés sont donnés miniscule et sans character spéciaux


def vigenere_cipher(message, key):
    ascii_letters = "abcdefghijklmnopqrstuvwxyz"
    key_nb = []  # pour stocker les indices de key
    message_nb = []  # pour stocker les indices du message
    coded_message = ""  # pour afficher le message à la fin

    # ce boucle trouve les indices du message en passant tout ce qui n'est pas des lettres
    for m in message.lower():
        if m in ascii_letters:
            message_nb += [ascii_letters.find(m)]
        else:
            message_nb.append(
                m
            )  # on stoche les espaces, les ponctuations, etc. directement

    # ce boucle trouve les indice du clef
    for k in key:
        key_nb += [ascii_letters.find(k)]

    # on va ajouter le key au message
    key_index = 0
    for i, e in enumerate(message_nb):
        if type(e) is int:
            message_nb[i] += key_nb[key_index % (len(key))]
            key_index += 1

    # on retransfere tout en lettre
    for i in range(len(message_nb)):
        if type(message_nb[i]) is int:
            coded_message += ascii_letters[message_nb[i] % 26]
        else:
            coded_message += message_nb[i]

    print(coded_message)
    return coded_message


# vigenere_cipher("this is my message", "key")
# vigenere_cipher("MesSaGGE2!", "clef")


def vigenere_decipher(message, key):
    ascii_letters = "abcdefghijklmnopqrstuvwxyz"
    key_nb = []  # pour stocker les indices de key
    message_nb = []  # pour stocker les indices du message
    decoded_message = ""  # pour afficher le message à la fin

    # ce boucle trouve les indices du message en passant tout ce qui n'est pas des lettres
    for m in message.lower():
        if m in ascii_letters:
            message_nb += [ascii_letters.find(m)]
        else:
            message_nb.append(
                m
            )  # on stoche les espaces, les ponctuations, etc. directement

    # ce boucle trouve les indice du clef
    for k in key:
        key_nb += [ascii_letters.find(k)]

    # on va ajouter le key au message
    key_index = 0
    for i, e in enumerate(message_nb):
        if type(e) is int:
            message_nb[i] -= key_nb[key_index % (len(key))]
            key_index += 1

    # on retransfere tout en lettre
    for i in range(len(message_nb)):
        if type(message_nb[i]) is int:
            decoded_message += ascii_letters[message_nb[i] % 26]
        else:
            decoded_message += message_nb[i]

    print(decoded_message)
    return decoded_message


# vigenere_decipher("dlgc mq wc kowqkkc", "key")
# vigenere_decipher("opwxcrkj2!", "clef")
