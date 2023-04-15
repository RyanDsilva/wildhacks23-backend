import os
from dotenv import load_dotenv

load_dotenv()

config = {
  "HOST": "127.0.0.1",
  "PORT": 5000,
  "DEBUG": True,
  "DB_HOST" : os.environ['MONGO_URL'],
  "JWT_KEY" : os.environ['JWT_KEY'],
  "TOKEN_EXPIRE_HOURS" : 12,
}