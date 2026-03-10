# Używamy obrazu Python jako podstawy
FROM python:3.12-slim

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy wszystkie pliki do kontenera
COPY . /app

# Instalujemy zależności z pliku requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Eksponujemy port 8080, ponieważ nasz serwer nasłuchuje na tym porcie
EXPOSE 8080

# Uruchamiamy serwer (zmieniamy polecenie uruchamiania na to, które chcesz)
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
