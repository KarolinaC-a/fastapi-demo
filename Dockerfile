# Użyj oficjalnego obrazu Pythona
FROM python:3.11-slim

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj plik z wymaganiami
COPY requirements.txt .

# Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj cały folder aplikacji do kontenera
COPY ./app /app/app

# Komenda uruchamiająca aplikację
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
