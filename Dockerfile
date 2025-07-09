# Python base image
FROM python:3.11-slim

# Setting working directory inside the container
WORKDIR /app

# Copying local files into working directory
COPY . .

# Installing dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exposing port for FastAPI to run on
EXPOSE 8000

# Starts app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]