import enum
from getkey import getkey
from tabulate import tabulate
from .BaseMenu import BaseMenu
from controller import Controller


class DepartmentMenu(BaseMenu):
    class Entry(enum.Enum):
        READ = (0, "Показать всех сотрудникув отдела и его главу")
        EXIT = (1, "Назад")

        def __init__(self, num, item):
            self.num = num
            self.item = item

    def __init__(self, db):
        super().__init__("Меню отделов: ", db)
        self.controller = Controller(self.db)

    def handle(self):
        if self.selected_entry == DepartmentMenu.Entry.READ.num:
            departments = self.controller.get_all_departments()
            for dep in departments:
                head = self.controller.get_employee(dep['head_id'])
                print(
                    f"{dep['description']}: {head['last_name']} {head['first_name']} ({head['email']})")

                dep_employees = self.controller.get_department_employees(
                    dep['id'])

                headers = ["ФИ", "Эл.адрес"]
                print(tabulate(dep_employees, headers=headers,
                      tablefmt="simple_grid"), "\n")
            getkey()
