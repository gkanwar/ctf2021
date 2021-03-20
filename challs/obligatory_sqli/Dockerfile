FROM python:3.8

WORKDIR /app

COPY src/ .
RUN pip install -r requirements.txt

CMD [ "python", "./server.py" ]