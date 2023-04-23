# Use an official Python runtime as the base image
FROM python:3.8

RUN mkdir -p /app

# Set the working directory in the container to /app
WORKDIR /app

# Copy requeriments to code
COPY requirements.txt /app/requirements.txt

# Copy requeriments to code
COPY . .

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Define the command to run the Flask production server
CMD gunicorn --bind 0.0.0.0:5000 -w 1 wsgi:app

