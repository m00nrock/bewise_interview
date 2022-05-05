FROM python:3.8.9

WORKDIR /backend

COPY requirements.txt /backend
RUN pip install -r requirements.txt
COPY . /backend
EXPOSE 5000