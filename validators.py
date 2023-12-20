from datetime import datetime

from prompt_toolkit.validation import ValidationError, Validator


class DateInputValidator(Validator):
    def validate(self, document):
        if not len(document.text) > 0:
            raise ValidationError(
                message="Input cannot be empty.",
                cursor_position=document.cursor_position,
            )
        try:
            _ = datetime.strptime(document.text, "%d.%m.%Y")
        except ValueError:
            raise ValidationError(
                message="Неверный формат даты!",
                cursor_position=document.cursor_position,
            )
