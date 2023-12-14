import enum
import inquirer
import sys
from simple_term_menu import TerminalMenu


class MainMenuEntry(enum.Enum):
    EMPLOYEES = (0, "Сотрудники")
    DEPARTMENTS = (1, "Отделы")
    CONTRACTS = (2, "Трудовые договора")
    VACATIONS = (3, "Отпуски")
    TRAINING = (4, "Обучение")
    PERFORMANCE_EVALUTION = (5, "Оценка производительности")

    def __init__(self, num, item):
        self.num = num
        self.item = item


def main_menu():
    return TerminalMenu(
        [entry.item for entry in MainMenuEntry],
        title="Главное меню:"
    )


def main():
    menu_entry_num = main_menu().show()
    if menu_entry_num == MainMenuEntry.EMPLOYEES.num:
        print("EMPLOYEES")
    elif menu_entry_num == MainMenuEntry.DEPARTMENTS.num:
        print("DEPARTMENTS")
    elif menu_entry_num == MainMenuEntry.CONTRACTS.num:
        print("CONTRACTS")
    elif menu_entry_num == MainMenuEntry.VACATIONS.num:
        print("VACATIONS")
    elif menu_entry_num == MainMenuEntry.TRAINING.num:
        print("TRAINING")
    elif menu_entry_num == MainMenuEntry.PERFORMANCE_EVALUTION.num:
        print("PERFORMANCE_EVALUTION")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
