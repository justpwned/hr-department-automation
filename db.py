import psycopg
from loguru import logger


class Database:
    def __init__(self, host, username, password, port, dbname):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.dbname = dbname
        self.conn = None

    def connect(self):
        if self.conn is None:
            try:
                self.conn = psycopg.connect(host=self.host,
                                            user=self.username,
                                            password=self.password,
                                            port=self.port,
                                            dbname=self.dbname)
            except psycopg.OperationalError as e:
                logger.error(e)
            finally:
                logger.info("Connection opened successfully")
