# Use a .NET SDK image as the base image
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build-env

# Set the working directory inside the container
WORKDIR /app

# Copy the C# source code into the container
COPY *.cs ./

# Create a new .NET project
RUN dotnet new console -n MyApp

# Copy the C# source code into the project directory
COPY main.cs ./MyApp/

# Change the working directory to the project directory
WORKDIR /app/MyApp

# Build the application
RUN dotnet build -c Release

# Create a runtime image based on the ASP.NET Core runtime
FROM mcr.microsoft.com/dotnet/runtime:7.0 AS runtime

# Set the working directory in the runtime image
WORKDIR /app

# Copy the compiled application from the build environment
COPY --from=build-env /app/MyApp/bin/Release/net7.0/ .

# Command to run the application
ENTRYPOINT ["dotnet", "MyApp.dll"]
