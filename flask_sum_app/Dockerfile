FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install -r requirement.txt

EXPOSE 80

ENTRYPOINT ["python", "app.py"]