# FROM python:3.8-alpine
FROM python:3.8-buster
COPY . /usr/src/app/
WORKDIR /usr/src/app/
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
EXPOSE 80
