# Use the full Python image
FROM python:3.13.2

# Install necessary build tools and libraries
RUN apt-get update && \
    apt-get install -y gcc g++ make cmake libopenblas-dev python3-dev gfortran && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements file for better caching
COPY requirements.txt /app/

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the files
COPY . /app/

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
