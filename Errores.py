COUNTRIES = {
    'mexico': 122,
    'argentina': 43,
    'colombia': 48,
    'ecuador': 15,
    'chile': 18,
}


def main():
    while True:
        country = str(input("Escribe el nombre de un pais: ")).lower()
        try:
            print("La poblacion de {} es {} millones".format(
                country, COUNTRIES[country]))
        except KeyError:
            print("No tenemos el dato de la poblacion de {}".format(country))
            print("Gracias Por Usar Este Programa")
            break


if __name__ == '__main__':
    main()
