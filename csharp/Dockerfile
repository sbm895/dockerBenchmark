# Utiliza la imagen base de SDK .NET Core
FROM mcr.microsoft.com/dotnet/sdk:latest

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos del directorio actual al directorio de trabajo en el contenedor
COPY . /app

# Compila el archivo Main.cs dentro del contenedor usando csc (compilador C#)
RUN dotnet new console -o temp && cp Main.cs temp/Program.cs && cd temp && dotnet run
