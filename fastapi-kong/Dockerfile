FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn

# Copy the rest of the application code
COPY . .

# Expose the port that the FastAPI app runs on
EXPOSE 8005

# Command to run the FastAPI app with uvicorn
CMD ["uvicorn", "main:app","--reload","--host", "0.0.0.0", "--port", "8005"]