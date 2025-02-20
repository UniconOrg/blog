FROM python:3.12-alpine

ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apk update \
    && apk add --no-cache \
        gcc \
        musl-dev \
        libffi-dev \
        openssl-dev \
    && pip install --upgrade pip \
    && pip install -U poetry

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN cd /tmp \
    && poetry export -f requirements.txt --output /app/requirements.txt --without-hashes --dev \
    && pip install --no-warn-script-location --disable-pip-version-check --no-cache-dir -r /app/requirements.txt \
    && apk del \
        gcc \
        musl-dev \
        libffi-dev \
        openssl-dev \
    && rm -rf /var/cache/apk/*

COPY ./src /app/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
