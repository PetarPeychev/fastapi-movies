FROM python:3.10-bookworm

WORKDIR /app

# Reduce image size by not writing bytecode
ENV PYTHONDONTWRITEBYTECODE 1

# Improve logging output by not buffering
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy service code
COPY movie_service movie_service
COPY _version.py README.md setup.py ./