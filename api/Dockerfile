# pull python image
FROM python:3.8-slim

# navigate to the app directory
WORKDIR /app

# copy the files from root into /app
COPY . .

RUN pip install --upgrade pip
# install requirements for fast-api upload be
RUN pip install -r requirements.txt

# expose port 8000 where the api will run from
EXPOSE 8000

# run api start up on docker run
CMD ["python", "main.py"]