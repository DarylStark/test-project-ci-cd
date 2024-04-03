FROM python:3.12-slim-bookworm

# Install dependencies
RUN apt update -y && apt install -y && apt install -y python3-poetry

# Creae and set working directory
RUN mkdir -p /app/src
WORKDIR /app/src

# Copy project files
COPY . .

# Install application
RUN poetry config virtualenvs.create false --local && \
    poetry install --no-interaction && \
    rm -rf /root/.cache/pypoetry

# Start the application
CMD ["test_project"]