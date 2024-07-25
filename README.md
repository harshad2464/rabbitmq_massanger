# rabbitmq_massanger
# install rabbitmq locally:
  - download rabbitmq file and install it
  - after installtion create queue for messages.
    
# Client script:
  - when a run client.py file then start pushing status to rabbitmq queue.

# Server script:
  - when a run server.py file then start consuming messages from rabbitmq and storing in mongodb database.

# run api for getting status count:
  - install python packages using command "pip install -r requirements.txt"
  - after installig packages start server using command "unvicorn main:app"

# database mongodb:
  - install mongodb database.
  - create database and then collection.
  - use this database for storing messages.
