# Temel imaj olarak Python 3.10 kullan
FROM python:3.11-slim

# Çalışma dizinini ayarlama
WORKDIR /app

# Gereksinimleri kopyalama
COPY requirements.txt .

# Gereksinimleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamanın kaynak kodunu kopyalama
COPY . .

# Uygulamayı başlat
CMD ["python", "app.py"]

# Uygulamanın dinleyeceği port
EXPOSE 5000
