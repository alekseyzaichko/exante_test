FROM python:3.7

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

COPY ./requirements.txt /
RUN pip install -r ./requirements.txt

COPY ./scripts/*.sh /
RUN chmod +x /*.sh

WORKDIR /app