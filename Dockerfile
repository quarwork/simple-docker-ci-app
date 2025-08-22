# Use the official lightweight Python 3.9 image based on Debian
# "slim" means minimal size, which reduces the image weight
FROM python:3.9-slim

# Set the working directory inside the container
# All following commands (COPY, RUN, CMD) will be executed inside this folder
WORKDIR /app

# Copy the dependency file (requirements.txt) into the container
# Copied separately for better caching (so dependencies don’t reinstall unnecessarily)
COPY requirements.txt .

# Install Python dependencies from requirements.txt
# --no-cache-dir removes pip cache after installation to keep the image small
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the container (to /app)
COPY . .

# Document that the application will listen on port 5000
# Flask runs on this port by default
EXPOSE 5000

# Define the default command to run when the container starts
# Start app.py using Python
CMD ["python", "app.py"]
