import sys
import os
from loguru import logger
from db import Database
from menu.MainMenu import MainMenu

from dotenv import load_dotenv

load_dotenv()


def main(db):
    main_menu = MainMenu(db)
    main_menu.loop()


if __name__ == "__main__":
    logger.remove()
    logger.add("execution.log")

    db = Database(os.environ.get("DATABASE_HOST"),
                  os.environ.get("DATABASE_USERNAME"),
                  os.environ.get("DATABASE_PASSWORD"),
                  os.environ.get("DATABASE_PORT"),
                  os.environ.get("DATABASE_NAME"))
    db.connect()
    try:
        main(db)
    except KeyboardInterrupt:
        sys.exit(0)
    finally:
        db.close()
        logger.info("Connection closed successfully")
