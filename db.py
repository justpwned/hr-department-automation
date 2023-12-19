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

    def define_schema_and_populate(self):
        try:
            with open('sql/schema.sql') as f:
                self.conn.execute(f.read())
            with open('sql/data.sql') as f:
                self.conn.execute(f.read())
        except psycopg.DatabaseError:
            logger.exception("Failed to populate database")
            self.conn.rollback()
        except OSError:
            logger.exception("Failed to open a file")
            self.conn.rollback()
        else:
            logger.info("Database schema has been successfully defined and"
                        "populated with data")
            self.conn.commit()

    def close(self):
        self.conn.close()
