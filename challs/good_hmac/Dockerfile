FROM python:3.8-slim

RUN apt-get update && apt-get install -y xinetd
COPY good_hmac.xinetd /etc/xinetd.d/good_hmac

RUN pip install pycryptodome

WORKDIR /app
COPY good_hmac.py flag.py ./

CMD [ "xinetd", "-dontfork" ]