
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build

COPY . /app

WORKDIR /app

EXPOSE 80

RUN dotnet new console -o MyApp && cp Program.cs MyApp/ && cd MyApp && dotnet publish -c Release -o out

FROM mcr.microsoft.com/dotnet/aspnet:6.0

WORKDIR /app

COPY --from=build /app/MyApp/out .

ENTRYPOINT ["dotnet", "MyApp.dll"]
