import os
from dotenv import load_dotenv

load_dotenv()

config = {
  "HOST": "0.0.0.0",
  "PORT": int(os.environ.get('PORT', 5000)),
  "DEBUG": False,
  "DB_HOST" : os.environ['MONGO_URL'],
  "JWT_KEY" : os.environ['JWT_KEY'],
  "TOKEN_EXPIRE_HOURS" : 12,
}