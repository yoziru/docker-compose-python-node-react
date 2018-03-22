FROM python:3.6
MAINTAINER yoziru-desu

RUN pip install -U pip setuptools
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . /app/backend
WORKDIR /app/backend

EXPOSE 8000

CMD ["python", "./src/server.py"]
