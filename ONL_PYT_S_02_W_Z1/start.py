import random


def RandomNumber():
    result = random.randint(1, 100)
    return result


def GetNumber(QuestionText):
    while True:
        try:
            result = int(input(QuestionText))
            return result
        except:
            print("It's not a number!")


def main():
    comp_nr = RandomNumber()
    human_nr = GetNumber('Guess the number: ')
    while True:
        if human_nr > comp_nr:
            print("Too big!")
            human_nr = GetNumber('Once again. Guess the number: ')
        elif human_nr < comp_nr:
            print("Too small!")
            human_nr = GetNumber('Once again. Guess the number: ')
        else:
            result = "You win!"
            return result


print(main())
