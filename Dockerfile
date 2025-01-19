#name has to be same

#dowmloading OS with python

FROM python:3.10-slim-bullseye

#creating app

WORKDIR /flask-loan-app

COPY artefacts/requirements.txt .

RUN pip3 install -r requirements.txt

COPY . /flask-loan-app/

CMD ["python","-m","flask","--app","app.py","run","--host=0.0.0.0","--port=8000"]

