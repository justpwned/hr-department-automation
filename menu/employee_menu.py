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
