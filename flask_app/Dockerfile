FROM python:3.8-alpine


WORKDIR /flask_app


COPY . .


RUN pip3 install --no-cache-dir -r requirements.txt


ENV FLASK_APP=App.py