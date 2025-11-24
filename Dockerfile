# Base image - simplified for game development
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies required for Pygame (headless)
# These are necessary for pygame to install and run (even if headless)
RUN apt-get update && apt-get install -y \
    libsdl2-2.0-0 \
    libsdl2-image-2.0-0 \
    libsdl2-mixer-2.0-0 \
    libsdl2-ttf-2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Default command (runs tests by default for safety)
CMD ["pytest"]

