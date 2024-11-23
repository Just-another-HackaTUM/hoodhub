# Django Projekt

## Installation

1. Klone das Repository:
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2. Erstelle und aktiviere eine virtuelle Umgebung:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3. Installiere die Abhängigkeiten:
    ```bash
    pip install -r requirements.txt
    ```

## Entwicklung

1. Starte den Entwicklungsserver:
    ```bash
    python manage.py runserver
    ```

2. Öffne deinen Browser und gehe zu `http://127.0.0.1:8000/`.

## Tests

1. Führe die Tests aus:
    ```bash
    python manage.py test
    ```

## create new app
```bash
python manage.py startapp <app-name>
```