import enum
from getkey import getkey
from tabulate import tabulate
from .BaseMenu import BaseMenu
from controller import Controller
from prompt import prompt_number, prompt_text, prompt_date


class VacationMenu(BaseMenu):
    class Entry(enum.Enum):
        READ = (0, "Посмотреть отпуска всех сотрудников")
        CREATE = (1, "Написать заявление на отпуск")
        EXIT = (2, "Назад")

        def __init__(self, num, item):
            self.num = num
            self.item = item

    def __init__(self, db):
        super().__init__("Меню отпусков: ", db)
        self.controller = Controller(self.db)

    def prompt_vacation(self):
        vacation = {}
        vacation["reason"] = prompt_text("Введите причину отпуска:")
        vacation["start_date"] = prompt_date("Начало отпуска:")
        vacation["end_date"] = prompt_date("Конец отпуска:")
        return vacation

    def handle(self):
        if self.selected_entry == VacationMenu.Entry.READ.num:
            employees = self.controller.get_all_employees()
            for emp in employees:
                emp_id = emp[0]
                emp_name = emp[1]
                emp_email = emp[4]

                emp_vacations = self.controller.get_all_employee_vacations(
                    emp_id)
                if len(emp_vacations) != 0:
                    print(f"Отпуска: {emp_name} ({emp_email})")
                    headers = ["Причина отпуска",
                               "Дата начала", "Дата окончания"]
                    print(tabulate(emp_vacations, headers=headers,
                          tablefmt="simple_grid"),  "\n")
            getkey()
        elif self.selected_entry == VacationMenu.Entry.CREATE.num:
            employee_id = prompt_number("Введите идентификатор сотрудника:")
            if employee_id in self.controller.get_valid_employee_ids():
                vacation = self.prompt_vacation()
                vacation["employee_id"] = employee_id
                self.controller.insert_vacation(vacation)
                print("Заявление в отпуск успешно принято")
            else:
                print(
                    f"Сотрудника с идентификатором {employee_id} не существует!")
            getkey()
