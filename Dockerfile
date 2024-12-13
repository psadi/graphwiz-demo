FROM ubuntu:24.04 AS base

RUN apt-get update -y && apt-get upgrade -y && \
  apt-get install --no-install-recommends -y python3-minimal python3-pip graphviz


FROM base AS builder

# USER daemon

WORKDIR app

COPY . .

RUN python3 -m pip install -r requirements.txt --break-system-packages

EXPOSE 8000

ENTRYPOINT [ "fastapi", "run", "main.py" ]
