# Image base in Python 3.7.4
FROM python:3.7.4

# Create dir code
WORKDIR /code

# Copy folders to base path
COPY ./doc /code/doc
COPY ./src /code/src

# Copy file to base path
COPY __main__.py /code/__main__.py
COPY requirements.txt /code/requirements.txt

# Install Requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Create auxiliar folders
RUN mkdir export

# Expose Port 9000
EXPOSE 9000

# Run code
CMD ["python","."]