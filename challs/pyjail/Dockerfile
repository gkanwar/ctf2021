FROM python:3.8-slim

RUN apt-get update && apt-get install -y xinetd
COPY pyjail.xinetd /etc/xinetd.d/pyjail

WORKDIR /app
COPY pyjail.py flag.txt ./

# CMD [ "python", "pyjail.py" ]
CMD [ "xinetd", "-dontfork" ]