FROM python:3.6.1-alpine

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN pip install flask==2.0.3

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

EXPOSE 5000

