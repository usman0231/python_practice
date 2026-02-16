from logs import Logger
from db import Connection

logger = Logger().get_log()
db = Connection()

### Create 100 random user