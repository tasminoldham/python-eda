FROM python:3.12.3

# setting the workingdir within the container
WORKDIR /app

# Install system packages required by pyodbc
RUN apt-get update && apt-get install -y build-essential unixodbc-dev

# Copy requirements.txt first
COPY requirements.txt /app/

# installing dependencies
RUN pip install -r requirements.txt

# copying the required files from the workingdir into the /app folder
COPY . /app


# on start
ENTRYPOINT ["python", "main.py"]

