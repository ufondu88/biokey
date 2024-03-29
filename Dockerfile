FROM python:3.8-slim

COPY requirements.txt /

RUN pip3 install --upgrade pip

RUN pip3 install -r /requirements.txt

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# Define the command to run the application
CMD ["gunicorn","--config", "gunicorn_config.py", "--reload", "main:app"]
