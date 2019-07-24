# Pull base image
FROM python:3.7-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /RoomScout

# Install dependencies
COPY requirements.txt /RoomScout/
RUN pip install -r requirements.txt
# Copy project
COPY . /RoomScout/
