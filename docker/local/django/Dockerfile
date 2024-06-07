FROM python:3.10.0-slim-buster

# Set environment variables
ENV APP_HOME=/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create application directories
RUN mkdir -p $APP_HOME/staticfiles

# Set the working directory to the app home
WORKDIR $APP_HOME

# Add metadata to the image to describe its contents and the maintainer
LABEL maintainer='api.imperfect@gmail.com'
LABEL youtube="https://www.youtube.com/c/APIImperfect"
LABEL description="Development image for Real Estate Project"

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gettext \
    netcat \
    gcc \
    default-mysql-client \
    pkg-config \
    libmariadb-dev-compat \
    libmariadb-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN pip3 install --no-cache-dir --upgrade pip

# Copy the requirements file and install Python dependencies
COPY ./requirements.txt $APP_HOME/requirements.txt
RUN pip3 install --no-cache-dir -r $APP_HOME/requirements.txt

# Ensure flower is installed
RUN pip3 install flower

# Copy entrypoint script, remove carriage return characters, and make it executable
COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint && chmod +x /entrypoint

# Copy start script, remove carriage return characters, and make it executable
COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start && chmod +x /start

# Copy celery worker start script, remove carriage return characters, and make it executable
COPY ./docker/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker && chmod +x /start-celeryworker

# Copy flower start script, remove carriage return characters, and make it executable
COPY ./docker/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower && chmod +x /start-flower

# Set the entrypoint
ENTRYPOINT ["/entrypoint"]
