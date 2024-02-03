FROM python:3.12.1-slim-bookworm

RUN mkdir /scrappy-bot
COPY . /scrappy-bot
COPY pyproject.toml /scrappy-bot

WORKDIR /scrappy-bot
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
CMD ["poetry", "run", "scrappy-bot"]