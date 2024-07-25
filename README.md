# rabbitmq_massanger
# Client script:
  - when a run client.py file ten start pushing status to rabbitmq.

# Server script:
  - when a run server.py file then start comsuming messages from rabbitmq and storing in mongodb database.

# run api for getting status count:
  - install python packages using command "pip install -r requirements.txt"
  - after installig packages start server using command "unvicorn main:app"

# database mongodb:
  - install mongodb database.
  - create database and then collection.
  - use thoes database for storing messages. 
