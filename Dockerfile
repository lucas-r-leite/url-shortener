# Use an official Python runtime as a parent image
FROM python:3.11.9-bookworm

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that the app will run on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
