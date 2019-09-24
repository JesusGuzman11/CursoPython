# -*- coding: utf-8 -*-

KEYS = {
    'a' : '°',
    'b' : '|',
    'c' : '¬',
    'd' : '!',
    'e' : '"',
    'f' : '#',
    'g' : '$',
    'h' : '%',
    'i' : '&',
    'j' : '/',
    'k' : '(',
    'l' : ')',
    'm' : '=',
    'n' : "'",
    'ñ' : '?',
    'o' : '¿',
    'p' : '¡',
    'q' : '+',
    'r' : '*',
    's' : '~',
    't' : '}',
    'u' : '{',
    'v' : '^',
    'w' : ']',
    'x' : ',',
    'y' : ';',
    'z' : '.',
    'A' : ':',
    'B' : '-',
    'C' : '_',
    'D' : ' ',
    'E' : '<',
    'F' : '>',
    'G' : '@',
    'H' : '♂',
    'I' : '♀',
    'J' : '○',
    'K' : '♪',
    'L' : '♫',
    'M' : '☼',
    'N' : '►',
    'Ñ' : '◄',
    'O' : '↕',
    'P' : '‼',
    'Q' : '¶',
    'R' : '§',
    'S' : '↨',
    'T' : '↑',
    'U' : '↓',
    'V' : '→',
    'W' : '←',
    'X' : '∟',
    'Y' : '↔',
    'Z' : '▲',
    '0' : '▼',
    '1' : '☺',
    '2' : '☻',
    '3' : '♥',
    '4' : '♦',
    '5' : '♣',
    '6' : '♠',
    '7' : '•',
    '8' : '◘',
    '9' : 'Ç',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}

def cypher(message):
    words = message.split(' ')
    cypher_message = []

    for word in words:
        cypher_word = ''
        for letter in word:
            cypher_word += KEYS[letter]

        cypher_message.append(cypher_word)

    return ' '.join(cypher_message)


def decipher(message):
    words = message.split(' ')
    decipher_message = []

    for word in words:
        decipher_word = ''

        for letter in word:

            for key, value in KEYS.items():
                if value == letter:
                    decipher_word += key

        decipher_message.append(decipher_word)

    return ' '.join(decipher_message)


def run():

    while True:

        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía. ¿Qué deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            message = str(input('Escribe tu mensaje: '))
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == 'd':
            message = str(input('Escribe tu mensaje tu cifrado: '))
            decypher_message = decipher(message)
            print(decypher_message)
        elif command == 's':
            print('salir')
            break
        else:
            print('¡Comando no encontrado!')


if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()