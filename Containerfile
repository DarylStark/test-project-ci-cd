FROM python:3.12-slim-bookworm

RUN pip3 install poetry

RUN mkdir -p /app/src

WORKDIR /app/src

COPY . .

RUN poetry config virtualenvs.create false --local
RUN poetry install --no-interaction
RUN rm -rf /root/.cache/pypoetry

CMD ["test_project"]