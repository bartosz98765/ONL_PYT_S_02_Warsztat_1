from flask import Flask, request
import random
app = Flask(__name__)\

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# @app.route('/')
# def main():
#     html = """
#     'Hello World'
#     <br>
#     <a href="/inna_strona"> Inna strona </a>
#     <br>
#     <a href="/hello2"> hello2 </a>
#     """
#     return html

@app.route('/hello2')
def hello2():
    return 'Hello Bartek!'

@app.route('/inna_strona')
def inna_strona():
    return 'To jest treść innej strony!<br>Zapraszam'

# @app.route('/dodaj/<int:a>/<int:b>')
# def dodaj(a, b):
#     return f"{a} + {b} = {int(a) + int(b)}"

@app.route('/dodaj', methods=['POST', 'GET'])
def dodaj():
    if request.method == 'GET':
        form = """
        <form method='POST' action='/dodaj'>
            <p>a : <input type='number' name='a'></p>
            <p>b : <input type='number' name='b'></p>
            <p><input type='submit'></p>
        </form>
        """
        return form
    else:
        a = int(request.form['a'])
        b = int(request.form['b'])
        return f"Wynik dodawania {a}+{b} = {a + b}"

@app.route('/losuj', methods=['POST', 'GET'])
def losuj():
    if request.method == 'GET':
        form = """
        <form method='POST' action='/losuj'>
            <p>a : <input type='number' name='a'>Podaj początek zakresu</p>
            <p>b : <input type='number' name='b'>Podaj koniec zakresu</p>
            <p><input type='submit' value='Wyślij liczby'></p>
        </form>
        """
        return form
    else:
        a = int(request.form['a'])
        b = int(request.form['b'])
        result = random.randint(a, b)
        return f"Wynik losowania: {result}"


@app.route('/rand/<int:a>/<int:b>')
def rand(a, b):
    if b <a:
        raise ValueError('b jest większe od a')
    rand_nr = random.randint(a, b)
    return f"Wylosowana liczba to {rand_nr}"


@app.route('/hello_name/<int:name>')
def hello_name(name):
    return f"Hello {name}"

@app.route('/')
def main():
    skowronek = """
    <a href="/hello"> hello</a>
    <a href="/hello2"> hello2</a>
    
    <form method='GET' action='/odbierz'>
        imie:<input type='text' name='imie'><br>
        <input type='submit' value='GET'><br>
    </form>
    
    <form method='POST' action='/odbierz'>
        imie:<input type='text' name='imie'><br>
        <input type='submit' value='POST'><br>
    </form>
    """
    return skowronek

@app.route('/odbierz', methods=['POST', 'GET'])
def odbierz():
    if request.method == 'GET':
        return f"otrzymałem informację GET imie o wartości {request.args['imie']}"
    else:
        return f"otrzymałem informację POST imie o wartości {request.form['imie']}"


#Dzień 4: Flask zadanie 6
@app.route('/lotek')
def lotek():
    x = list(range(1, 50))
    random.shuffle(x)
    x = x[:6]
    x.sort()
    return f"<p>wylosowano {x}</p>"

#Dzień 4: Flask zadanie 7
@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    if request.method == 'GET':
        form = """
        <form method='POST' action='/welcome'>
            Podaj swoje imię:<input type='text' name='imie'><br>
            <input type='submit' value='POST'><br>
        </form>
        """
        return form
    else:
        return f"<p>Witaj {request.form['imie']}</p>"


#Dzień 4: Flask zadanie 8
@app.route('/calc', methods=['POST', 'GET'])
def calc():
    if request.method == 'GET':
        form = """
        <form method='POST' action='/welcome'>
            Podaj pierwszą liczbę: <input type='number' name='a'><br>
            Podaj drugą liczbę: <input type='number' name='b'><br> 
            <label for="select">Wybierz działanie</label>
              <select name='operacja'>
                <option value='+'>Dodawanie</option>
                <option value='-'>Odejmowanie</option>
                <option value='*'>Mnożenie</option>
                <option value='/'>Dzielenie</option>
              </select>
              <input type='submit' value='Wynik'><br>
        </form>
      """
        return form
    else:
        a = int(request.form['a'])
        b = int(request.form['b'])

        result = a + b

        return f"<p>Wynik: {a} {request.form['operacja']} {b} = {result}</p>"

@app.route('/kalkulator', methods=['GET', 'POST'])
def kalkulator():
    operacje = {'+':'dodawanie', '-':'odejmowanie', '*':'mnozenie', '/':'dzielenie'}
    if request.method == 'GET':
        form = """
         <form method='POST' >
            <p>abc : <input type='number' name='a'></p>
            <p>def : <input type='number' name='b'></p>
            <p>
            <select name='opr'>
              <option value='+'>+</option>
              <option value='-'>-</option>
              <option value='*'>*</option>
              <option value='/'>/</option>
            </select>
            </p>
            <p><input type='submit'></p>
        </form>        """
        return form
    a = int(request.form.get('a'))
    b = int(request.form.get('b'))
    opr = request.form.get('opr')
    if opr == '+':
        result = a + b
    elif opr == '-':
        result = a - b
    elif opr == '*':
        result = a * b
    else:
        result = a / b
    return f" wynik to {result}"

@app.route("/losowanka", methods=['GET', 'POST'])
def losowanka():
    powitanie = 'Zagrajmy w zgadywanie liczb'
    number = int(request.form.get('number', random.randint(1, 100)))
    if request.method == 'POST':
        try:
            zgadnij = int(request.form.get('zgadnij'))
        except:
            zgadnij = 999
        if zgadnij == number:
            number =  random.randint(1, 100)
            odp = 'zgadłeś'
            powitanie = 'Wylosowałem nową liczbę. Zagrajmy jeszcze raz.'
        elif zgadnij > number:
            odp = "za dużo"
        else:
            odp = "za mało"
    else:
        odp = ""

    form = f"""
    <p>{powitanie}<p>
    <form method='POST'>
        <input type='hidden' name='number' value='{number}'>
        <input type='number' name='zgadnij'>
        <input type='submit' value='ok' name='action'>
    </form>
    <p>{odp}</p>
    """
    return form

#---------------------------------------------------------------------------

@app.route('/zgadywanieliczb', methods=['GET', 'POST'])
def zgadywanieliczb():
    min = int(request.form.get('min', 0))
    max = int(request.form.get('max', 1000))
    i = 0
    tmp = 0
    odp = ''

    if request.method == 'POST':
        guess = int((max - min) / 2) + min
        odp = f'Typuje liczbę: {guess}'
        tmp = guess
        i = int(request.form.get('i'))
        if i > 1:
            answer = request.form.get('answer')
            if answer == 'zamalo':
                min = int(request.form.get('tmp'))
                guess = int((max - min) / 2) + min
                odp = f'Typuje liczbę: {guess}'
                tmp = guess
            elif answer == 'zaduzo':
                max = int(request.form.get('tmp'))
                guess = int((max - min) / 2) + min
                odp = f'Typuje liczbę: {guess}'
                tmp = guess
            else:
                odp = 'Thank you. If you want to play again, press any button'
                min = 0
                max = 1000
                i = 0
    else:
        odp = ""

    form = f"""
         <form method='POST'>
         <p>
            Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach</br>
            Jeśli jesteś gotowy wciśnij dowolny przycisk, rozpocznę zgadywanie
         </p>
            <input type='hidden' name='min' value='{min}'>
            <input type='hidden' name='max' value='{max}'>
            <input type='hidden' name='tmp' value='{tmp}'>
            <input type='hidden' name='i' value='{i+1}'>
         </p>
            <button type="submit" value='zaduzo' name='answer'><strong>Too big</strong></button>
            <button type="submit" value='zamalo' name='answer'><strong>Too small</strong></button>
            <button type="submit" value='ok' name='answer'><strong>You win</strong></button></br>
         </p>
         <p>{odp}</p>
         </form> 
        """

    return form




if __name__ == '__main__':
    app.run()