print('Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach')
input("Jeśli jesteś gotowy wciśnij dowolny przycisk, rozpocznę zgadywanie")

def humananswer():
    result = input("""
    Wybierz:
    1 - jeśli za mało
    2 - jeśli za dużo
    3 - jeśli zgadłem 
    """)
    while result not in ('1', '2', '3'):
        result = input('Błędna wartość! Wybierz z listy: ')
    return result

min = 0
max = 1000
answer = ''
i = 1

while answer != '3':
    guess = int((max - min) / 2) + min
    print(f'{i}: Zgaduję: {guess}')
    i += 1
    answer = humananswer()
    if answer == '1':
        min = guess
    elif answer == '2':
        max = guess

print('Wygrałem')

