# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV APP_HOME=/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create application subdirectory for static files
RUN mkdir -p $APP_HOME/staticfiles

# Set the working directory to the app home
WORKDIR $APP_HOME

# Add metadata to the image to describe its contents and the maintainer
LABEL maintainer='vbm7752@gmail.com'
LABEL twitter='@victormidega'
LABEL description="Development image for Real Estate Project"

# Install system dependencies
RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gettext \
    netcat-openbsd \
    gcc \
    default-mysql-client \
    libmariadb-dev-compat \
    libmariadb-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN pip3 install --no-cache-dir --upgrade pip

# Copy the requirements file and install Python dependencies
COPY ./requirements.txt $APP_HOME/requirements.txt
RUN pip3 install --no-cache-dir -r $APP_HOME/requirements.txt

# Copy entrypoint script, remove carriage return characters, and make it executable
COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint && chmod +x /entrypoint

# Copy start script, remove carriage return characters, and make it executable
COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start && chmod +x /start

# Define the entrypoint for the container
ENTRYPOINT ["/entrypoint"]
