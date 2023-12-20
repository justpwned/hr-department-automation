import enum
from loguru import logger
from .BaseMenu import BaseMenu
from .EmployeeMenu import EmployeeMenu
from .DepartmentMenu import DepartmentMenu
from .VacationMenu import VacationMenu
from getkey import getkey


class MainMenu(BaseMenu):
    class Entry(enum.Enum):
        EMPLOYEES = (0, "Сотрудники")
        DEPARTMENTS = (1, "Отделы")
        VACATIONS = (2, "Отпуски")
        PERFORMANCE_EVALUATION = (3, "Оценка производительности")
        POPULATE_DB = (4, "Установить схему и заполнить базу данных")
        EXIT = (5, "Выход")

        def __init__(self, num, item):
            self.num = num
            self.item = item

    def __init__(self, db):
        super().__init__("Главное меню: ", db)

    def handle(self):
        if self.selected_entry == MainMenu.Entry.EMPLOYEES.num:
            menu = EmployeeMenu(self.db)
            menu.loop()
        elif self.selected_entry == MainMenu.Entry.DEPARTMENTS.num:
            menu = DepartmentMenu(self.db)
            menu.loop()
        elif self.selected_entry == MainMenu.Entry.VACATIONS.num:
            menu = VacationMenu(self.db)
            menu.loop()
        elif self.selected_entry == MainMenu.Entry.PERFORMANCE_EVALUATION.num:
            logger.info("PERFORMANCE_EVALUATION MENU ENTRY SELECTED")
        elif self.selected_entry == MainMenu.Entry.POPULATE_DB.num:
            self.db.define_schema_and_populate()
            getkey()
