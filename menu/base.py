from simple_term_menu import TerminalMenu


class BaseMenu:
    def __init__(self, title):
        self.title = title

    def show(self):
        self.selected_entry = TerminalMenu(
            [entry.item for entry in self.Entry],
            title=self.title
        ).show()
