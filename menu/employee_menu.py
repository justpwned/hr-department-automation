import enum
from loguru import logger
from .base import BaseMenu


class EmployeeMenu(BaseMenu):
    class Entry(enum.Enum):
        READ = (0, "Показать всех сотрудников")
        UPDATE = (1, "Редактировать информацию о сотрудниках")
        DELETE = (2, "Удалить сотрудника")
        CREATE = (3, "Добавить сотрудника")

        def __init__(self, num, item):
            self.num = num
            self.item = item

    def __init__(self):
        super().__init__("Меню сотрудников: ")

    def handle(self,  db):
        if self.selected_entry == EmployeeMenu.Entry.READ.num:
            logger.info("READ EMPLOYEE")
        elif self.selected_entry == EmployeeMenu.Entry.UPDATE.num:
            logger.info("UPDATE EMPLOYEE")
        elif self.selected_entry == EmployeeMenu.Entry.DELETE.num:
            logger.info("DELETE EMPLOYEE")
        elif self.selected_entry == EmployeeMenu.Entry.CREATE.num:
            logger.info("CREATE EMPLOYEE")
