FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy app source
COPY . /code/

# In Dockerfile (optional if you're using volumes):
RUN mkdir -p /code/staticfiles