
FROM openjdk:11-jdk-slim

COPY . /app

WORKDIR /app

RUN javac Main.java

EXPOSE 80

CMD ["java", "main"]
