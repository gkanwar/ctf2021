FROM python:3.8-slim

RUN apt-get update && apt-get install -y xinetd
COPY pyjail.xinetd /etc/xinetd.d/pyjail

RUN pip install RestrictedPython

WORKDIR /app
COPY pyjail.py flag.py ./

CMD [ "xinetd", "-dontfork" ]