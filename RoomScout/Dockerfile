# pull official base image
FROM python:3.7-alpine

# set work directory
WORKDIR /usr/src/RoomScout

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/RoomScout/Pipfile
RUN pipenv install --skip-lock --system --dev

# copy project
COPY . /usr/src/RoomScout/
