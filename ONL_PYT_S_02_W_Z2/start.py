import random


def randomnumberlist(rbeg, rend, howmany):
    numbers = random.sample(range(rbeg, rend), howmany)
    return numbers


def getnumber(QuestionText):
    while True:
        try:
            result = int(input(QuestionText))
            return result
        except:
            print("It's not a number!")

human_nr = []
result = []
comp_nr = randomnumberlist(1, 49, 6)

human_nr = human_nr.append(getnumber('Podaj liczbę: '))
while len(human_nr) < 6:
    tmp = getnumber('Podaj liczbę: ')
    if tmp not in human_nr:
        human_nr = human_nr.append(tmp)

print(sorted(human_nr))
print(sorted(comp_nr))

for element in human_nr:
    if element in comp_nr:
        result = result.append(element)

#    result = [result.append(for element in human_nr[i]:) for i in range(5) if human_nr]
print('Poprawnie wytypowałeś następujące liczby: {result}')
