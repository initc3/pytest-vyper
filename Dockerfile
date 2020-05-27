FROM python:latest

WORKDIR /usr/src/pytest-vyper

COPY . .

RUN pip install --upgrade pip
RUN pip install --editable .[dev]
