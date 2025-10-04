FROM python:3.9-slim

ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "run"]
