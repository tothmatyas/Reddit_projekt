# Reddit Klon - Django projekt

Egyszerű Reddit-szerű webalkalmazás Django használatával.

## Funkciók
- Regisztráció
- Bejelentkezés / kijelentkezés
- Új poszt létrehozása
- Képfeltöltés
- Kommentelés
- Like rendszer
- Keresés cím alapján
- Saját posztok megtekintése
- Saját poszt törlése

## Telepítés és futtatás

### 1. Repository klónozása
```bash
git clone IDE_JON_A_REPO_LINK
cd reddit-django

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

http://127.0.0.1:8000

python manage.py createsuperuser
