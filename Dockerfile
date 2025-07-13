FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential gcc

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=5000

CMD ["sh", "-c", "python init_db.py && python app.py"]
