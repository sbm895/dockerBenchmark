# Utiliza la imagen base de Alpine Linux
FROM alpine:latest

# Instala GCC para compilar el código C
RUN apk update && apk add --no-cache gcc musl-dev

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos del directorio actual al directorio de trabajo en el contenedor
COPY . /app

# Compila main.c dentro del contenedor usando GCC
RUN gcc main.c -o main

# Establece la instrucción por defecto para ejecutar el programa compilado cuando se inicie el contenedor
CMD ["./main"]
