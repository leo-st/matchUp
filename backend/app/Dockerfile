FROM python:3.10.5-bullseye

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc netcat wget unixodbc iputils-ping telnet && \
    apt-get clean -y

# Install Python dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install --requirement /requirements.txt

# Create directory for the app user
RUN mkdir -p /home/app

# Create the app user
RUN groupadd -g 1000 app
RUN useradd -m -u 1000 -g 1000 app

# Create the appropriate directories
ENV HOME=/home
ENV APP_HOME=/home/app

# Copy the application files
COPY . $APP_HOME

# Create data and logs directories (use -p to avoid errors if they already exist)
RUN mkdir -p $APP_HOME/data
RUN mkdir -p $APP_HOME/data/logs

WORKDIR $APP_HOME

# Chown all the files to the app user
RUN chown -R app:app $HOME
RUN chown -R 1000:1000 $APP_HOME/data/

# Change to the app user
USER app

# Run entrypoint.sh
ENTRYPOINT ["sh", "/home/app/api/entrypoint.sh"]