from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def kalkulator():
    wynik = None
    if request.method == "POST":
        try:
            liczba1 = float(request.form["liczba1"])
            liczba2 = request.form.get("liczba2")
            operacja = request.form["operacja"]

            if operacja in ["dodaj", "odejmij", "pomnóż", "podziel", "potęga"] and liczba2 == "":
                wynik = "Błąd: Brak drugiej liczby"
            else:
                liczba2 = float(liczba2) if liczba2 else 0

                if operacja == "dodaj":
                    wynik = liczba1 + liczba2
                elif operacja == "odejmij":
                    wynik = liczba1 - liczba2
                elif operacja == "pomnóż":
                    wynik = liczba1 * liczba2
                elif operacja == "podziel":
                    if liczba2 != 0:
                        wynik = liczba1 / liczba2
                    else:
                        wynik = "Błąd: Dzielenie przez zero"
                elif operacja == "potęga":
                    wynik = liczba1 ** liczba2
                elif operacja == "pierwiastek":
                    if liczba1 >= 0:
                        wynik = math.sqrt(liczba1)
                    else:
                        wynik = "Błąd: Pierwiastek z liczby ujemnej"
        except ValueError:
            wynik = "Błąd: Nieprawidłowe dane wejściowe"

    return render_template("index.html", wynik=wynik)

if __name__ == "__main__":
    app.run(debug=True)
