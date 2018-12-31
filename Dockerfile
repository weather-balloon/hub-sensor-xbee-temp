FROM python:3.6-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY *.py ./

CMD /app/app.py
