from .base import BaseMenu
from .employee_menu import EmployeeMenu
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

    def __init__(self):
        super().__init__("Главное меню: ")

    def handle(self,  db):
        if self.selected_entry == MainMenu.Entry.EMPLOYEES.num:
            logger.info("EMPLOYEE MENU ENTRY SELECTED")
            menu = EmployeeMenu()
            menu.show()
            menu.handle(db)
        elif self.selected_entry == MainMenu.Entry.DEPARTMENTS.num:
            logger.info("DEPARTMENTS MENU ENTRY SELECTED")
        elif self.selected_entry == MainMenu.Entry.CONTRACTS.num:
            logger.info("CONTRACTS MENU ENTRY SELECTED")
        elif self.selected_entry == MainMenu.Entry.VACATIONS.num:
            logger.info("VACATIONS MENU ENTRY SELECTED")
        elif self.selected_entry == MainMenu.Entry.TRAINING.num:
            logger.info("TRAINING MENU ENTRY SELECTED")
        elif self.selected_entry == MainMenu.Entry.PERFORMANCE_EVALUATION.num:
            logger.info("PERFORMANCE_EVALUATION MENU ENTRY SELECTED")
        elif self.selected_entry == MainMenu.Entry.POPULATE_DB.num:
            logger.info("POPULATE DATABASE MENU ENTRY SELECTED")
            db.define_schema_and_populate()
