from flask import Flask, request, jsonify, render_template
import math
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/oblicz", methods=["POST"])
def oblicz():
    dane = request.json
    wyrazenie = dane.get("wyrazenie", "")

    try:
        # Bezpieczne przekształcenie wyrażenia: zamień ^ na **, √ na math.sqrt
        wyrazenie = wyrazenie.replace("^", "**")
        wyrazenie = re.sub(r"√(\d+(\.\d+)?)", r"math.sqrt(\1)", wyrazenie)

        # Zbiór dozwolonych funkcji
        bezpieczny_kontekst = {
            "math": math,
            "__builtins__": {}
        }

        wynik = eval(wyrazenie, bezpieczny_kontekst)
        return jsonify({"wynik": wynik})
    except Exception as e:
        return jsonify({"blad": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
