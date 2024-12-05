FROM python:3.10-slim

WORKDIR /app

RUN pip install flask prometheus-client

COPY app.py .
COPY metrics.py .

EXPOSE 5000

CMD ["python", "app.py"]
