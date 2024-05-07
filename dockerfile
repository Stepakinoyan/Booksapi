FROM python:3.11

# 
WORKDIR /code


COPY /pyproject.toml /code
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install 
COPY . .