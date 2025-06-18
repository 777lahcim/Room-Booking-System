# Używamy oficjalnego obrazu Pythona
FROM python:3.11-slim

# Ustawiamy katalog roboczy w kontenerze
WORKDIR /app

# Kopiujemy plik z zależnościami
COPY requirements.txt .

# Instalujemy zależności
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy cały kod projektu
COPY . .

# Otwieramy port na którym działa Django
EXPOSE 8000

# Domyślne polecenie uruchamiające serwer
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
