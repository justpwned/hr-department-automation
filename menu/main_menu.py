from .base import BaseMenu
import enum
from loguru import logger


class MainMenu(BaseMenu):
    class Entry(enum.Enum):
        EMPLOYEES = (0, "Сотрудники")
        DEPARTMENTS = (1, "Отделы")
        CONTRACTS = (2, "Трудовые договора")
        VACATIONS = (3, "Отпуски")
        TRAINING = (4, "Обучение")
        PERFORMANCE_EVALUATION = (5, "Оценка производительности")
        REPORTS = (6, "Отчеты")
        POPULATE_DB = (7, "Определить схему и заполнить базу данных")

        def __init__(self, num, item):
            self.num = num
            self.item = item

    def handle(self, entry_num, db):
        if entry_num == MainMenu.Entry.EMPLOYEES.num:
            logger.info("EMPLOYEES")
            # view_employees()
            # edit_employee()
            # remove_employee()
            # add_employee()
        elif entry_num == MainMenu.Entry.DEPARTMENTS.num:
            logger.info("DEPARTMENTS")
        elif entry_num == MainMenu.Entry.CONTRACTS.num:
            logger.info("CONTRACTS")
        elif entry_num == MainMenu.Entry.VACATIONS.num:
            logger.info("VACATIONS")
        elif entry_num == MainMenu.Entry.TRAINING.num:
            logger.info("TRAINING")
        elif entry_num == MainMenu.Entry.PERFORMANCE_EVALUATION.num:
            logger.info("PERFORMANCE_EVALUATION")
        elif entry_num == MainMenu.Entry.POPULATE_DB.num:
            db.define_schema_and_populate()
