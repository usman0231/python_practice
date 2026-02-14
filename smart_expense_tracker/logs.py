import logging

class  Logger:
    def __init__ (self, level, msg, name):
        self.level = level
        self.msg = msg
        self.name = name
        
    def log(self):
        logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        )

        
        logger = logging.getLogger(self.name)
        logger.info(self.msg)