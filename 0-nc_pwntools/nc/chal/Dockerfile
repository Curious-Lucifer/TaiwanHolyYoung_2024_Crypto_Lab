FROM alpine:3.18

RUN apk add --no-cache python3 py3-pip socat

RUN mkdir -p /chal
WORKDIR /chal

COPY ./src /chal

CMD ["socat", "TCP-LISTEN:20000,fork", "EXEC:'python3 /chal/server.py'"]
