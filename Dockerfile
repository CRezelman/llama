FROM python:3.12.4

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT 8000

CMD exec gunicorn --bind :${PORT} --workers 1 --threads 8 app.app:app