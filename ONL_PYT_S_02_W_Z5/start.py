import random


def cube(size, throws, addition):
    result = addition
    for i in range(throws):
        result += random.randint(1, size)
    return result


def humaninput(cubetypes):
    print(f"""
    Dostępne kostki to: {cubetypes}
    Kod rzutu powinien być w notacji: xDy+z
    gdzie:
    y – rodzaj kostek, których należy użyć (np. D6, D10),
    x – liczba rzutów kośćmi; jeśli rzucamy raz, ten parametr jest pomijalny,
    z – liczba, którą należy dodać (lub odjąć) do wyniku rzutów (opcjonalnie)
    """)


def checkcubetype(cubecode, cubetypes):
    position = -1
    for cubetype in cubetypes:
        position = cubecode.find(cubetype)
        if position != -1:
            return cubetype, position
    return None


def checkthrows(cubecode, position):
    throws = 1
    if position > 0:
        try:
            throws = int(cubecode[0:position])
            return throws
        except:
            print('Niepoprawny kod!')
            return None
    return throws

def checkaddition(cubecode, cubetypes):
    addition = None
    if '+' in cubecode:
        try:
            position = cubecode.find('+')
            addition = int(cubecode[(position + 1):])
        except:
            print('Niepoprawny kod!')
            return None
    elif '-' in cubecode:
        try:
            position = cubecode.find('-')
            addition = -int(cubecode[(position + 1):])
        except:
            print('Niepoprawny kod!')
            return None
    elif cubecode[-2:] in cubetypes:
        addition = 0
        return addition
    return addition


def getcorrectinput(cubetypes):
    while True:
        cubecode = input("Podaj kod: ")
        cubetype, position = checkcubetype(cubecode, cubetypes)
        if cubetype == None:
            return

        throw = checkthrows(cubecode, position)
        if throw == None:
            return

        addition = checkaddition(cubecode, cubetypes)
        if addition == None:
            return
        else:
            return [cubetype, throw, addition]


def main():
    cubetypes = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
    cubetype = None
    throw = None
    addition = None

    humaninput(cubetypes)


    while cubetype == None or throw == None or addition == None:
        try:
            cubetype, throw, addition = getcorrectinput(cubetypes)
        except:
            print('Błędny kod!')

    size = int(cubetype[1:])

    print(cubetype, throw, addition)

    result = cube(int(size), int(throw), int(addition))

    print(f'Wynik rzutu: {result}')

    return



main()
