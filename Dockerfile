# Use the official Python image
FROM python:3.12-slim 

# Set environment variable to ensure Python output is not buffered
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set working directory
WORKDIR /src

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY ./src /src

EXPOSE 8000

