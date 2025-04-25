FROM python:3.12-alpine

# Set the working directory
WORKDIR /app

# Install build dependencies and git
RUN apk add --no-cache git

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Optionally remove git (if not needed at runtime)
RUN apk del git

# Copy application files
COPY . .

# Command to run the application
CMD ["python", "app.py"]
