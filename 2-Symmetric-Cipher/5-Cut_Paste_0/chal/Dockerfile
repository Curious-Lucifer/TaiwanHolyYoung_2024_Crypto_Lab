FROM alpine:3.18

RUN apk add --no-cache python3 py3-pip

RUN pip3 install pycryptodome flask
WORKDIR /chal

COPY ./src /chal

CMD ["flask", "run", "--host=0.0.0.0"]
