FROM python:3.12-slim-bookworm

# Install dependencies
RUN apt-get update -y && \
    apt-get install --no-install-recommends -y python3-poetry=1.3.2+dfsg-3 python3-distutils=3.11.2-3 python3-apt=2.6.0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

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