# Base image
FROM python:3.10-slim-buster

# Set working directory
WORKDIR /code

# Copy requirements file
COPY requirements.txt .
COPY ./nlp_api /code/nlp_api

# Install spaCy and its dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        build-essential \
        libpq-dev \
        git && \
        pip install spacy uvicorn pydantic fastapi[all] && \
    python -m spacy download en_core_web_sm

CMD ["sh"]
EXPOSE 8000