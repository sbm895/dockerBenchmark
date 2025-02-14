# Utiliza la imagen base de Node.js
FROM node:latest

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos del directorio actual al directorio de trabajo en el contenedor
COPY . /app

# Establece la instrucción por defecto para ejecutar main.js cuando se inicie el contenedor
CMD ["node", "main.js"]
