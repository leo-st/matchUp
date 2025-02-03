FROM postgres:16-bullseye

RUN apt-get update \
    && apt-get -y install netcat git build-essential postgresql-server-dev-16 pgagent iputils-ping telnet\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/db

RUN userdel postgres 
RUN groupadd -g 1000 postgres 
RUN useradd -m -u 1000 -g 1000 postgres

ENV HOME=/home/db

COPY 000_access_control.sql /docker-entrypoint-initdb.d/000_access_control.sql
COPY 001_feed.sql /docker-entrypoint-initdb.d/001_feed.sql
COPY 002_messages.sql /docker-entrypoint-initdb.d/002_messages.sql


RUN mkdir -p /postgresql_data
RUN chown -R 1000:1000 /postgresql_data

ENV PGDATA=/postgresql_data

# Start PostgreSQL
CMD ["postgres"]