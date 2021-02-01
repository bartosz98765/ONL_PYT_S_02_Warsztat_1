import random


def cube(size=6, throws=1, addition=0):
    result = addition
    for i in range(throws):
        result += random.randint(1, size)
    return result


def cubechoosencomp(cubetypes):
    cubetype = cubetypes[random.randint(0, 7)]
    size = int(cubetype[1:])
    return size


# def playerthrows(whothrow, cubechoosen1, cubechoosen2, cubetypes):
#
#     throw_1 = cube()
#
#     return actualplayerscore

def humaninput(cubetypes):
    print(f"""
    Dostępne kostki to: {cubetypes}
    Podaj kod kostki w notacji: Dy
    gdzie: y – liczba ścian kostki (np. D6, D10),
    """)


def checkcubetype(cubecode, cubetypes):
    position = -1
    for cubetype in cubetypes:
        if cubecode == cubetype:
            return cubecode
    return None


def getcorrectinput(cubetypes):
    while True:
        cubecode = input("Podaj kod: ")
        cubetype = checkcubetype(cubecode, cubetypes)
        if cubetype != None:
            size = int(cubetype[1:])
            return size
        else:
            print('Błędny kod!')


def main():
    cubetypes = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
    cubetype = None
    throw_nr = 1

    humaninput(cubetypes)

    cubesize1 = getcorrectinput(cubetypes)
    cubesize2 = getcorrectinput(cubetypes)
    throw_1 = cube(cubesize1)
    throw_2 = cube(cubesize2)
    humanscore = throw_1 + throw_2
    print(throw_nr, humanscore)

    compcubesize1 = cubechoosencomp(cubetypes)
    compcubesize2 = cubechoosencomp(cubetypes)
    compthrow_1 = cube(compcubesize1)
    compthrow_2 = cube(compcubesize2)
    compscore = compthrow_1 + compthrow_2
    print(throw_nr, compscore)

    throw_nr = 2
    print(f'Wynik gracza: {humanscore} | Wynik komputera: {compscore}')
    input()

    while humanscore < 2001 and compscore < 2001:
        cubesize1 = getcorrectinput(cubetypes)
        cubesize2 = getcorrectinput(cubetypes)
        throw_1 = cube(cubesize1)
        throw_2 = cube(cubesize2)
        throw_nr += 1
        if (throw_1 + throw_2) == 7:
            humanscore = humanscore // 7
        elif (throw_1 + throw_2) == 11:
            humanscore = humanscore * 11
        else:
            humanscore = humanscore + throw_1 + throw_2
        print(f"{throw_nr}, D:{cubesize1} {throw_1}, D:{cubesize2} {throw_2}, Wynik człowieka: {humanscore}")

        compcubesize1 = cubechoosencomp(cubetypes)
        compcubesize2 = cubechoosencomp(cubetypes)
        compthrow_1 = cube(compcubesize1)
        compthrow_2 = cube(compcubesize2)
        if (compthrow_1 + compthrow_2) == 7:
            compscore = compscore // 7
        elif (compthrow_1 + compthrow_2) == 11:
            compscore = compscore * 11
        else:
            compscore = compscore + compthrow_1 + compthrow_2
        print(f"{throw_nr}, D:{compcubesize1}, {compthrow_1}, D:{compcubesize2}, {compthrow_2}, Wynik:{compscore}")

        print(f'Wynik gracza: {humanscore} | Wynik komputera: {compscore}')
        input()

    if humanscore > compscore:
        print(f"Wygrał gracz")
    else:
        print(f"Wygrał komputer")

    return


main()
