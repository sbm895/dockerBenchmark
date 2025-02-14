FROM golang:1.23.6-bookworm

WORKDIR /app

COPY . /app

RUN go build -o app main.go

CMD ["./app"]
