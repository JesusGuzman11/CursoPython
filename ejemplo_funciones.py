# -*- coding: utf-8 -*-

import turtle

def main():
    window = turtle.Screen()
    jesus = turtle.Turtle()

    make_square(jesus)

    turtle.mainloop()

def make_square(jesus):
    length = int(input('Tamaño de cuadrado: '))

    for i in range(4):
        make_line_and_turn(jesus, length)

def make_line_and_turn(jesus, length):
    jesus.forward(length)
    jesus.left(90)

if __name__ == '__main__':
    main()