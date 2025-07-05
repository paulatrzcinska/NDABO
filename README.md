# NDABO - Prosta Aplikacja Kalkulatorowa

NDABO to prosta aplikacja kalkulatora internetowego, która umożliwia wykonywanie podstawowych operacji matematycznych w przeglądarce. Projekt zrealizowany z użyciem HTML, CSS oraz Pythona (Flask) po stronie serwera.

## Funkcje

- Dodawanie, odejmowanie, mnożenie, dzielenie
- Interaktywny interfejs webowy
- Obsługa przez prosty backend w Pythonie (Flask)

## Technologie

- **HTML**, **CSS** – warstwa front-endowa
- **Python (Flask)** – backend do obsługi logiki i żądań
- **Render** – platforma do hostowania aplikacji

## Instrukcja uruchomienia lokalnie

1. **Sklonuj repozytorium:**
   ```bash
   git clone https://github.com/paulatrzcinska/NDABO.git
   cd NDABO
   ```

2. **Utwórz wirtualne środowisko i zainstaluj zależności:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # lub venv\Scripts\activate na Windows
   pip install -r requirements.txt
   ```

3. **Uruchom aplikację:**
   ```bash
   python app.py
   ```

4. Aplikacja będzie dostępna pod adresem `http://localhost:5000`.

## Deployment na Render

Aplikacja została wdrożona za pomocą platformy **Render**.

 [Zobacz działającą aplikację](https://ndabo.onrender.com/)

### Jak wdrożyć samodzielnie?

1. Utwórz konto na [render.com](https://render.com)
2. Połącz je z GitHubem i wybierz repozytorium `NDABO`
3. Wybierz typ usługi: **Web Service**
4. Ustaw:
   - Build command: `pip install -r requirements.txt`
   - Start command: `python app.py` lub użyj `gunicorn` jeśli aplikacja jest produkcyjna
   - Port: domyślnie `5000`
5. Render automatycznie uruchomi Twoją aplikację
