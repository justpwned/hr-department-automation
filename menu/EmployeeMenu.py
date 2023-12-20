import enum
from loguru import logger
from getkey import getkey
from InquirerPy import inquirer
from tabulate import tabulate
from .BaseMenu import BaseMenu
from controller import Controller
from prompt import prompt_text, prompt_date, prompt_number
from datetime import datetime


class EmployeeMenu(BaseMenu):
    class Entry(enum.Enum):
        SHOW = (0, "Показать всех сотрудников")
        HIRE = (1, "Нанять сотрудника")
        FIRE = (2, "Уволить сотрудника")
        EXIT = (3, "Назад")

        def __init__(self, num, item):
            self.num = num
            self.item = item

    def __init__(self, db):
        super().__init__("Меню сотрудников: ", db)
        self.controller = Controller(self.db)

    def prompt_employee(self):
        employee = {}

        employee["last_name"] = prompt_text("Введитие фамилию:")
        employee["first_name"] = prompt_text("Введите имя:")
        employee["email"] = prompt_text("Введите эд.адрес:")
        employee["date_of_birth"] = prompt_date("Введите дату рождения:")
        employee["gender"] = inquirer.select(
            message="Выберите пол:",
            choices=[
                "Мужской",
                "Женский"
            ],
            filter=lambda v: 'F' if v == "Женский" else "M"
        ).execute()

        departments = self.controller.get_all_departments()

        employee["department_id"] = inquirer.select(
            message="Выберите отдел:",
            choices=[f"{i['id']}: {i['description']}" for i in departments],
            filter=lambda v: v.split(":")[0]
        ).execute()

        return employee

    def prompt_contract(self):
        contract = {}

        contract["conclusion_date"] = datetime.today()
        contract["job_title"] = prompt_text("Введите должность:")
        contract["salary"] = prompt_number("Введите зарплату в рублях:")

        return contract

    def prompt_education(self):
        education = {}

        education["description"] = prompt_text("Образование:")
        education["graduation_date"] = prompt_date("Дата окончания:")

        return education

    def handle(self):
        if self.selected_entry == EmployeeMenu.Entry.SHOW.num:
            employees = self.controller.get_all_employees()

            headers = ["№", "ФИ",  "Дата рождения", "Пол",
                       "Эл.почта", "Должность", "Зарплата"]
            print(tabulate(employees, headers=headers, tablefmt="simple_grid"))
            print(f"Количество сотрудников: {len(employees)}")

            getkey()
        elif self.selected_entry == EmployeeMenu.Entry.HIRE.num:
            employee = self.prompt_employee()
            employee_id = self.controller.insert_employee(employee)

            contract = self.prompt_contract()
            self.controller.insert_contract(contract, employee_id)

            education = self.prompt_education()
            self.controller.insert_education(education, employee_id)

            print("Новый сотрудник был успешно записан в базу данных")
            getkey()
        elif self.selected_entry == EmployeeMenu.Entry.FIRE.num:
            employee_id = prompt_number("Введите идентификатор сотрудника:")
            deleted_entries = self.controller.delete_employee(employee_id)
            if deleted_entries is None:
                print(
                    f"Сотрудника с идентификатором {employee_id} не существует")
            else:
                print(
                    f"Сотрудника с идентификатором {employee_id} был успешно уволен")
            getkey()
