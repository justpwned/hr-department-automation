from psycopg.rows import dict_row
import itertools


class Controller:
    def __init__(self, db):
        self.db = db

    def get_all_employees(self):
        query = ("SELECT emp.id, CONCAT(emp.last_name, ' ', emp.first_name), "
                 "to_char(emp.date_of_birth, 'DD.MM.YYYY'), "
                 "CASE "
                 "WHEN emp.gender = 'F' THEN 'Жен' "
                 "WHEN emp.gender = 'M' THEN 'Муж' "
                 "END, "
                 "emp.email, cont.job_title, CONCAT(cont.salary, ' ₽') "
                 "FROM \"Employee\" AS emp "
                 "JOIN \"WorkContract\" AS cont on emp.id = cont.employee_id")

        employees = self.db.conn.execute(query).fetchall()
        return employees

    def get_valid_employee_ids(self):
        query = "SELECT id FROM \"Employee\""
        employee_ids = itertools.chain(*self.db.conn.execute(query).fetchall())
        return employee_ids

    def get_employee(self, id):
        query = "SELECT * FROM \"Employee\" WHERE id=%s"
        with self.db.conn.cursor(row_factory=dict_row) as cur:
            employee = cur.execute(query, (id,)).fetchone()
        return employee

    def get_all_departments(self):
        query = "SELECT * FROM \"Department\""
        with self.db.conn.cursor(row_factory=dict_row) as cur:
            departments = cur.execute(query).fetchall()
        return departments

    def get_department_employees(self, department_id):
        query = ("SELECT CONCAT(last_name, ' ', first_name), email "
                 "FROM \"Employee\" "
                 "WHERE department_id = %s "
                 "ORDER BY last_name")
        employees = self.db.conn.execute(query, (department_id, )).fetchall()
        return employees

    def insert_employee(self, employee):
        query = ("INSERT INTO \"Employee\" (first_name, last_name, date_of_birth, gender, email) "
                 "VALUES (%s, %s, %s, %s, %s) RETURNING id")
        id = self.db.conn.execute(query,
                                  (employee["first_name"], employee["last_name"], employee["date_of_birth"], employee["gender"], employee["email"])).fetchone()
        self.db.conn.commit()
        return id[0]

    def insert_contract(self, contract, employee_id):
        query = ("INSERT INTO \"WorkContract\" (conclusion_date, job_title, salary, employee_id) "
                 "VALUES (%s, %s, %s, %s)")
        self.db.conn.execute(
            query, (contract["conclusion_date"], contract["job_title"], contract["salary"], employee_id))
        self.db.conn.commit()

    def insert_education(self, education, employee_id):
        query = ("INSERT INTO \"Education\" (description, graduation_date, employee_id) "
                 "VALUES (%s, %s, %s)")
        self.db.conn.execute(
            query, (education["description"], education["graduation_date"], employee_id))
        self.db.conn.commit()

    def delete_employee(self, employee_id):
        query = "DELETE FROM \"Employee\" WHERE id = %s RETURNING *"
        deleted_entries = self.db.conn.execute(
            query, (employee_id, )).fetchone()
        self.db.conn.commit()
        return deleted_entries

    def get_all_employee_vacations(self, employee_id):
        query = ("SELECT reason, start_date, end_date "
                 "FROM \"Vacation\" "
                 "WHERE employee_id = %s")
        emp_vacations = self.db.conn.execute(query, (employee_id, )).fetchall()
        return emp_vacations

    def insert_vacation(self, vacation):
        query = ("INSERT INTO \"Vacation\" (reason, start_date, end_date, employee_id) "
                 "VALUES (%s, %s, %s, %s)")
        self.db.conn.execute(
            query, (vacation["reason"], vacation["start_date"], vacation["end_date"], vacation["employee_id"]))
        self.db.conn.commit()
