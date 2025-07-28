# fastapi-demo 🚀

To jest prosta aplikacja FastAPI hostowana na Railway.
Temat: Kalendarz z rejestracją zadań
Cel: Stworzenie aplikacji webowej z backendem w FastAPI, frontendem w React + Tailwind CSS, konteneryzacją w Dockerze i wdrożeniem na Railway.
Opis funkcjonalności aplikacji
Użytkownik może:
Dodawać zadania do kalendarza
 Oznaczać je jako wykonane
 Przeglądać zadania według daty
✨ Endpointy API

- `GET /greet/{name}` — zwraca powitanie

Przykład:
https://fastapi-demo-production-ccd1.up.railway.app/greet/Karolina

🚀 Deployment

Aplikacja jest wdrożona na Railway:  
👉 [Link do aplikacji](https://fastapi-demo-production-ccd1.up.railway.app)

🛠️ Uruchomienie lokalnie

```bash
pip install -r requirements.txt, uvicorn, main:app --reload

---

### 🚀 Jak dodać plik na GitHub?

1. Utwórz plik `README.md` lokalnie lub online przez GitHub:
   - Wejdź do repozytorium
   - Kliknij `Add file` > `Create new file`
   - Nazwij go `README.md`
   - Wklej zawartość
   - Zatwierdź (`Commit new file`)
# 🐍 FastAPI Demo — prosta aplikacja API

Projekt pokazowy API zbudowany w Pythonie przy użyciu **FastAPI**, wdrożony na **Railway** oraz konteneryzowany za pomocą **Dockera**. 
Pozwala na szybkie testowanie prostych zapytań HTTP.

---

## 🚀 Wersja online

🔗 [Kliknij, aby uruchomić aplikację](https://twoja-aplikacja.railway.app)  
*(Zamień na swój link z Railway!)*

---

## 🧰 Technologie

- Python
- FastAPI
- Docker
- Railway (hosting)
- Pytest (testowanie)

---

🐳 Uruchamianie w Dockerze

`bash
docker build -t fastapi-demo .
docker run -p 8000:8000 fastapi-demo

---

🔍 Przykładowe zapytanie

`http
GET /hello?name=Karolina
```

📥 Odpowiedź:
```json
{
  "message": "Hello Karolina"
}
```

---

🧪 Testowanie

```bash
pytest -v
```
📷 Screenshot
 ![Podgląd aplikacji](assets/demo.png)


---

📄 Pliki

- `App/main.py` — główny kod aplikacji
- `requirements.txt` — zależności
- `Dockerfile` — konfiguracja Dockera

---

📦 Deployment przez Railway

Wdrożenie odbywa się przez [Railway](https://railway.app) na podstawie domyślnych ustawień. Możesz dodać plik `railway.json` lub używać GUI.

---

📬 Kontakt

Masz pytania lub chcesz rozwinąć aplikację? Napisz do mnie! 😄  
📧 `kciuborska@gmail.com` 
```





