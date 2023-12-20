CREATE TABLE "Employee" (
    id serial PRIMARY KEY,
    first_name text NOT NULL, last_name text NOT NULL, date_of_birth date NOT NULL,
    gender character(1) NOT NULL,
    email text NOT NULL,
    department_id integer,
    CONSTRAINT gender_check CHECK (gender in ('M', 'F'))
);

CREATE TABLE "Department" (
    id serial PRIMARY KEY,
    description text NOT NULL,
    head_id integer,
    CONSTRAINT FK_department_employee FOREIGN KEY (head_id) REFERENCES "Employee"(id)
);

ALTER TABLE "Employee" ADD CONSTRAINT FK_employee_department FOREIGN KEY (department_id) REFERENCES "Department"(id);

CREATE TABLE "Education" (
    id serial PRIMARY KEY,
    description text NOT NULL,
    graduation_date date NOT NULL,
    employee_id integer NOT NULL,
    CONSTRAINT FK_education_employee FOREIGN KEY (employee_id) REFERENCES "Employee"(id)
);


CREATE TABLE "PerformanceEvaluation" (
    id serial PRIMARY KEY,
    evaluation_date date NOT NULL,
    rating integer NOT NULL,
    comment text NOT NULL,
    employee_id integer NOT NULL,
    CONSTRAINT rating_check CHECK (rating BETWEEN 1 AND 5),
    CONSTRAINT FK_performanceevaluation_employee FOREIGN KEY (employee_id) REFERENCES "Employee"(id) ON DELETE CASCADE
);

CREATE TABLE "Vacation" (
    id serial PRIMARY KEY,
    reason text NOT NULL,
    start_date date NOT NULL,
    end_date date NOT NULL,
    employee_id integer NOT NULL,
    CONSTRAINT FK_vacation_employee FOREIGN KEY (employee_id) REFERENCES "Employee"(id) ON DELETE CASCADE
);

CREATE TABLE "WorkContract" (
    id serial PRIMARY KEY,
    conclusion_date date NOT NULL,
    job_title text NOT NULL,
    salary integer NOT NULL,
    employee_id integer NOT NULL,
    CONSTRAINT salary_check CHECK (salary > 0),
    CONSTRAINT FK_workcontract_employee FOREIGN KEY (employee_id) REFERENCES "Employee"(id) ON DELETE CASCADE
);
