FROM ubuntu:22.04 AS builder-image

ARG DEBIAN_FRONTEND=noninteractive
# ENV TZ="Asia/Kolkata"

RUN apt-get update && apt-get install --no-install-recommends -y python3.10 python3.10-dev python3.10-venv python3-pip python3-wheel build-essential && \
	apt-get clean && rm -rf /var/lib/apt/lists/*
    
RUN apt-get update --no-install-recommends -y
RUN apt-get install libpq-dev python3.10-dev --no-install-recommends -y

# ENV TZ="Asia/Kolkata"

COPY requirements.txt .
RUN python3.10 -m pip install -r requirements.txt

COPY . .

EXPOSE 8000


CMD ["python3", "manage.py", "runserver"]