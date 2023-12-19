import enum
from loguru import logger
from .BaseMenu import BaseMenu
from .EmployeeMenu import EmployeeMenu


class MainMenu(BaseMenu):
    class Entry(enum.Enum):
        EMPLOYEES = (0, "Сотрудники")
        DEPARTMENTS = (1, "Отделы")
        CONTRACTS = (2, "Трудовые договора")
        VACATIONS = (3, "Отпуски")
        TRAINING = (4, "Обучение")
        PERFORMANCE_EVALUATION = (5, "Оценка производительности")
        POPULATE_DB = (6, "Установить схему и заполнить базу данных")
        EXIT = (7, "Выход")

        def __init__(self, num, item):
            self.num = num
            self.item = item

    def __init__(self, db):
        super().__init__("Главное меню: ", db)

    def handle(self):
        if self.selected_entry == MainMenu.Entry.EMPLOYEES.num:
            logger.info("EMPLOYEE MENU ENTRY SELECTED")
            menu = EmployeeMenu(self.db)
            menu.loop()
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
            self.db.define_schema_and_populate()
