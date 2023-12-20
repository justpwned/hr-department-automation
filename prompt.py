from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator
from validators import DateInputValidator
from datetime import datetime


def prompt_id(message, invalid_message, valid_ids):
    return inquirer.number(
        message=message,
        min_allowed=1,
        validate=lambda v: len(v) > 0 and int(v) in valid_ids(),
        invalid_message=invalid_message,
        filter=lambda v: int(v),
    ).execute()


def prompt_number(message):
    return inquirer.number(
        message=message,
        validate=EmptyInputValidator("Поле не может быть пустым!"),
    ).execute()


def prompt_text(message):
    return inquirer.text(
        message=message,
        validate=EmptyInputValidator("Поле не может быть пустым!")).execute()


def prompt_date(message):
    return inquirer.text(
        message=message,
        filter=lambda v: datetime.strptime(v, "%d.%m.%Y").date(),
        validate=DateInputValidator(),
        invalid_message="Неверный формат даты!").execute()
