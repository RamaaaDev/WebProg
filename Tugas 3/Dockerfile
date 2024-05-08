FROM python:3.10-slim-buster

# Buat direktori kerja
WORKDIR /mysite

# Salin file requirements.txt dan instal dependensinya
COPY requirements.txt .

# Upgrade pip dan instal dependensi Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Salin seluruh konten dari direktori mysite lokal ke dalam kontainer
COPY mysite/ .

# Expose port 5000
EXPOSE 5000

# Jalankan server menggunakan manage.py
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
