#les import
import string

#les textes à étudier + dictionaire

LANGUAGE_PROFILES = {
    "english": {
        "e": 12.7, "t": 9.1, "a": 8.2, "o": 7.5, "i": 7.0, "n": 6.7, "s": 6.3, "h": 6.1, "r": 6.0, "d": 4.3, "l": 4.0, "c": 2.8, "u": 2.8, "m": 2.4, "w": 2.4, "f": 2.2, "g": 2.0, "y": 2.0, "p": 1.9, "b": 1.5, "v": 1.0, "k": 0.8, "j": 0.2, "x": 0.2, "q": 0.1, "z": 0.1
    },
    "french": {
        "e": 14.7, "a": 7.6, "i": 7.5, "s": 7.9, "n": 7.2, "r": 6.6, "t": 7.0, "o": 5.8, "l": 5.5, "u": 6.3, "d": 3.7, "c": 3.3, "m": 2.7, "p": 3.0, "v": 1.8, "q": 1.4, "f": 1.1, "b": 0.9, "g": 1.0, "h": 1.1, "j": 0.3, "x": 0.4, "y": 0.3, "z": 0.1, "é": 1.5, "è": 0.8, "ê": 0.6, "ë": 0.1, "à": 0.5, "ù": 0.1, "ç": 0.3
    },
    "spanish": {
        "e": 13.7, "a": 12.5, "o": 8.7, "s": 7.9, "n": 7.0, "r": 6.9, "l": 5.2, "d": 5.0, "c": 4.7, "t": 4.6, "u": 3.9, "m": 3.2, "p": 2.5, "b": 1.4, "g": 1.0, "v": 0.9, "y": 1.0, "q": 1.0, "h": 0.7, "f": 0.5, "z": 0.4, "j": 0.5, "ñ": 0.3, "á": 0.4, "é": 0.4, "í": 0.4, "ó": 0.4, "ú": 0.4
    },
    "portuguese": {
        "a": 14.6, "e": 12.6, "o": 10.7, "s": 7.8, "r": 6.7, "i": 6.2, "n": 5.0, "d": 4.9, "m": 4.7, "u": 4.6, "t": 4.3, "c": 3.9, "l": 2.8, "p": 2.5, "v": 1.6, "g": 1.3, "h": 1.2, "q": 1.2, "b": 1.0, "f": 1.0, "z": 0.5, "j": 0.4, "x": 0.2, "á": 0.5, "â": 0.3, "ã": 0.5, "é": 0.4, "ê": 0.2, "í": 0.2, "ó": 0.4, "ô": 0.2, "õ": 0.3, "ú": 0.2, "ç": 0.3
    },
    "italian": {
        "e": 11.8, "a": 11.7, "i": 10.7, "o": 9.8, "n": 6.9, "l": 6.5, "r": 6.4, "t": 5.6, "s": 4.9, "c": 4.5, "d": 3.7, "u": 3.2, "m": 2.9, "p": 3.0, "v": 2.1, "g": 1.6, "h": 0.6, "b": 1.0, "f": 1.1, "z": 1.0, "à": 0.2, "è": 0.2, "é": 0.2, "ì": 0.2, "ò": 0.2, "ù": 0.2
    },
    "german": {
        "e": 17.4, "n": 9.8, "i": 7.6, "s": 7.3, "r": 7.0, "a": 6.5, "t": 6.2, "d": 5.1, "h": 4.8, "u": 4.3, "l": 3.4, "c": 3.1, "g": 3.0, "m": 2.5, "o": 2.5, "b": 1.9, "w": 1.9, "f": 1.7, "k": 1.2, "z": 1.1, "ä": 0.6, "ö": 0.4, "ü": 0.7, "ß": 0.3, "j": 0.3, "v": 0.8
    },
    "dutch": {
        "e": 18.9, "n": 10.0, "a": 7.5, "t": 6.8, "i": 6.5, "r": 6.4, "o": 6.1, "d": 5.6, "s": 3.7, "l": 3.6, "g": 3.4, "v": 2.8, "h": 2.4, "k": 2.3, "m": 2.2, "u": 1.9, "b": 1.6, "p": 1.6, "w": 1.5, "j": 1.5, "z": 1.4, "f": 0.8, "c": 0.6, "x": 0.1, "y": 0.1, "é": 0.2, "è": 0.1, "ë": 0.1
    },
    "swedish": {
        "e": 10.2, "a": 9.4, "n": 8.6, "t": 7.7, "r": 8.4, "s": 6.6, "l": 5.3, "d": 4.7, "o": 4.5, "i": 4.8, "m": 3.5, "g": 2.9, "k": 3.1, "v": 2.4, "h": 2.1, "u": 1.9, "f": 2.0, "b": 1.3, "p": 1.8, "å": 1.3, "ä": 1.8, "ö": 1.3, "y": 0.6, "j": 0.6
    },
    "polish": {
        "a": 8.9, "i": 8.2, "e": 7.7, "o": 7.6, "z": 6.2, "n": 5.5, "r": 4.7, "w": 4.7, "y": 4.0, "c": 3.9, "l": 3.7, "t": 3.3, "s": 3.2, "d": 2.5, "k": 2.5, "p": 2.4, "m": 2.4, "u": 2.4, "j": 2.3, "b": 1.5, "g": 1.5, "ę": 1.1, "ł": 2.1, "ś": 0.8, "ń": 0.8, "ć": 0.8, "ó": 0.7, "ź": 0.3, "ż": 0.4
    },
    "turkish": {
        "a": 12.9, "e": 8.6, "i": 8.3, "n": 7.9, "r": 6.7,"l": 6.0, "d": 5.2, "k": 4.7, "t": 3.6, "u": 3.2, "m": 3.0, "o": 2.9, "b": 2.8, "s": 2.7, "y": 2.7, "v": 2.4, "z": 1.5, "g": 1.3, "ç": 1.2, "ş": 1.2, "ğ": 1.1, "ı": 5.1, "ö": 0.8, "ü": 0.9, "c": 0.7, "h": 0.6, "f": 0.5, "j": 0.4, "p": 0.3
    },
    "esperanto": {
        "a": 12.0, "e": 8.9, "i": 10.0, "o": 9.8, "u": 9.4, "n": 8.5, "l": 6.1, "s": 5.7, "r": 5.6, "t": 4.8, "k": 4.5, "m": 3.7, "d": 3.5, "p": 3.1, "v": 2.1, "g": 2.0, "b": 1.8, "f": 1.4, "h": 1.2, "ĉ": 1.0, "ĝ": 0.8, "ĵ": 0.5, "ŝ": 0.6, "ŭ": 0.3, "ĥ": 0.2, "z": 0.3, "c": 0.3, "j": 0.6
    }
}

text1="Un texte est une série orale ou écrite de mots perçus comme constituant un ensemble cohérent, porteur de sens et utilisant les structures propres à une langue (conjugaisons, construction et association des phrases…)[1]. Un texte n'a pas de longueur déterminée sauf dans le cas de poèmes à forme fixe comme le sonnet ou le haïku."
text2="It goes without saying that humans (mammals identifiable as those that stand upright and are comparatively advanced and capable of detailed thought) have pretty remarkable bodies, given all that they've accomplished. (Furthermore, an especially intelligent human brain produced this text!) To be sure, humans have overcome predators, disease, and all sorts of other obstacles over thousands of years. To fully understand and appreciate these accomplishments, let's take at some of the most well-known parts of the human body! The head, or the spherical body part that contains the brain and rests at the top of the human body, has quite a few individual organs and body parts on it. (It should quickly be mentioned that hair occupies the space on top of the head, and the ears, the organs responsible for hearing, are located on either side of the head.) From top to bottom, the eyebrows, or horizontal strips of hair that can be found above the eye, are the first components of the head. The eyes are below them, and are round, orb-like organs that allow humans to see. The eyes make way for the nose, or an external (sticking-out) organ that plays an important part in the breathing and bacteria-elimination processes. Below that is the mouth, or a wide, cavernous organ that chews food, removes bacteria, helps with breathing, and more. The mouth contains teeth, or small, white-colored, pointed body parts used to chew food, and the tongue, or a red-colored, boneless organ used to chew food and speak. The neck is the long body part that connects the head to the chest (the muscular body part that protects the heart and lungs), and the stomach, or the part of the body that contains food and liquid-processing organs, comes below that. The legs are the long, muscular body parts that allow humans to move from one spot to another and perform a variety of actions. Each leg contains a thigh (a thick, especially muscular body part used to perform strenuous motions; the upper part of the leg) and a calf (thinner, more flexible body part that absorbs the shock associated with movement; the lower part of the leg). Feet can be found at the bottom of legs, and each foot is comprised of five toes, or small appendages that help balance. Arms are long, powerful body parts that are located on either side of chest, below the shoulders;arms are comprised of biceps (the thicker, more powerful upper portion), and forearms (the thinner, more flexible lower portion). Hands, or small, gripping body parts used for a tremendous number of actions, are at the end of arms. Each hand contains five fingers, or small appendages used to grip objects. The aforementioned shoulders are rounded body parts that aid arms' flexibility. One's back is found on the opposite side of the stomach, and is a flat section of the body that contains important muscles that're intended to protect the lungs and other internal organs, in addition to helping humans perform certain motions and actions."
text3="Tekst – wypowiedź (zwłaszcza utrwalona graficznie, ale także ustnie) powstała w obrębie określonego systemu językowego, stanowiąca zamkniętą i skończoną całość z punktu widzenia treściowego. W tym znaczeniu tekstem jest zarówno wypowiedź jednozdaniowa (lub równoważnik zdania), jak i wielozdaniowa (np. dzieło literackie)."
text4="Ellen woont in Canada en ze gaat op vakantie naar Europa. De vliegreis naar Europa duurt ruim zeven uur. Ellen bezoekt Duitsland, Zwitserland, Hongarije, Spanje en Frankrijk. In de laatste week van haar vakantie reist ze met de trein van Parijs naar Nederland. Ze gaat naar Volendam en Delft. Ze gaat ook een dag naar Amsterdam.Ellen huurt een fiets in Amsterdam. Ze wil graag een musea bezoeken want ze houdt van kunst. Eerst bezoekt ze het Rijksmuseum op het Museumplein. Van alle schilderijen van de kunstenaar Rembrandt van Rijn vindt ze De Nachtwacht het mooiste. Het is een heel groot schilderij. Hij schilderde De Nachtwacht in Het Rembrandthuis. Het Rembrandthuis is nu ook een museum. Vroeger woonde Rembrandt van Rijn in dat gebouw. 's Middags fietst Ellen naar het Stedelijk Museum en bekijkt er moderne kunst. In het Van Gogh Museum ziet ze de schilderijen van Vincent van Gogh. Die vindt ze ook heel erg mooi. Pas laat in de middag gaat ze toch nog even naar Artis. Dat is een dierentuin in Amsterdam. Ellen ziet er allerlei dieren, zoals apen, giraffes en krokodillen. Aan het eind van de dag brengt Ellen de fiets terug. Ze gaat met de tram naar haar hotel."
text5="Hela familjen Jansson älskar djur och de besöker djurparken så ofta de kan. Josefin tycker att aporna är bäst. De sitter högt uppe i träden ovanför alla nyfikna besökare. En gång kom en apa närmare och ställde sig rakt framför Josefin. De stod länge och tittade på varandra, men sedan sprang apan i väg och gömde sig bakom en buske. Christoffer tycker mest om sälarna. De kan sitta och vila på en sten i solen och i nästa ögonblick dyka och försvinna under vattenytan. Mamma Lenas favoritdjur är lejonen. Speciellt lejonungarna är så söta! De brukar leka med varandra tills de blir så trötta att de bara ligger i en hög på varandra. Om de plötsligt blir rädda sätter de sig bredvid sin mamma. För pappa Tom är fiskarna mest fascinerande. Han står länge vid de vackra och rogivande akvarierna för att se på de färggranna fiskarna."
#### étape 1 : trier les characteres + enlever les points etc. + tourner le compteur en pourcentage

def letter_perc(text):
    text=text.lower()
    char=[] #liste de nos caracteres
    data=[] #liste pour compter cb fois la caractere à l'indice associé apparait

    for letter in text:
        #on enleve tout ce qui n'est pas une lettre
        if letter in string.punctuation or letter == " " or letter == "...": #jsp pq ... ça s'enleve pas avec ponctuation
            pass
        
        elif letter in char:
            i = char.index(letter)
            data[i] += 1
        else:
            char.append(letter)
            data.append(1)
    
    #on fait compte --> pourcentage
    total=sum(data)
    data = [i/total*100 for i in data]
    
    return [char,data]

""" 
print(letter_perc(text1))
print(letter_perc(text2))
print(letter_perc(text3))
"""

#### étape 2: on compare les donnés

def language_guesser(text):
    eval_text=letter_perc(text)

    delta_compa=[[],[]]

    for lang in LANGUAGE_PROFILES:
        delta = 0

        for i in range (len(eval_text[0])):
            letter = eval_text[0][i]

            if letter in LANGUAGE_PROFILES[lang]: 
                delta += abs(eval_text[1][i] - LANGUAGE_PROFILES[lang][letter])

            else:
                pass
        
        delta_compa[0].append(lang)
        delta_compa[1].append(delta)
    
    val_min=min(delta_compa[1])
    guess=delta_compa[1].index(val_min)


    print("the language is", delta_compa[0][guess])
    return delta_compa[0][guess]

print(language_guesser(text1))
print(language_guesser(text2))
print(language_guesser(text3))
print(language_guesser(text4))
print(language_guesser(text5))