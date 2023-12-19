from loguru import logger
from tabulate import tabulate


class EmployeeController:
    def __init__(self, db):
        self.db = db

    def show_employees(self):
        logger.info("SHOWING EMPLOYEES TABLE")
        query = ("SELECT emp.id, CONCAT(emp.last_name, ' ', emp.first_name), "
                 "to_char(emp.date_of_birth, 'DD.MM.YYYY'), "
                 "CASE "
                 "WHEN emp.gender = 'F' THEN 'Жен' "
                 "WHEN emp.gender = 'M' THEN 'Муж' "
                 "END, "
                 "emp.email, cont.job_title, CONCAT(cont.salary::numeric, ' ₽') "
                 "FROM \"Employee\" AS emp "
                 "JOIN \"WorkContract\" AS cont on emp.id = cont.employee_id")

        employees = self.db.conn.execute(query).fetchall()
        headers = ["№", "ФИ",  "Дата рождения",
                   "Пол",  "Эл.почта", "Должность", "Зарплата"]
        print(tabulate(employees, headers=headers, tablefmt="simple_grid"))
        print(f"Количество сотрудников: {len(employees)}")
