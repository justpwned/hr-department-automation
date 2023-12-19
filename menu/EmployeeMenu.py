import enum
from loguru import logger
from getkey import getkey
from .BaseMenu import BaseMenu
from controllers.EmployeeController import EmployeeController


class EmployeeMenu(BaseMenu):
    class Entry(enum.Enum):
        READ = (0, "Показать всех сотрудников")
        UPDATE = (1, "Редактировать информацию о сотрудниках")
        DELETE = (2, "Удалить сотрудника")
        CREATE = (3, "Добавить сотрудника")
        EXIT = (4, "Назад")

        def __init__(self, num, item):
            self.num = num
            self.item = item

    def __init__(self, db):
        super().__init__("Меню сотрудников: ", db)

    def handle(self):
        emp_controller = EmployeeController(self.db)
        if self.selected_entry == EmployeeMenu.Entry.READ.num:
            logger.info("READ EMPLOYEE")
            emp_controller.show_employees()
            getkey()
        elif self.selected_entry == EmployeeMenu.Entry.UPDATE.num:
            logger.info("UPDATE EMPLOYEE")
        elif self.selected_entry == EmployeeMenu.Entry.DELETE.num:
            logger.info("DELETE EMPLOYEE")
        elif self.selected_entry == EmployeeMenu.Entry.CREATE.num:
            logger.info("CREATE EMPLOYEE")
