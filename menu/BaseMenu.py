from simple_term_menu import TerminalMenu


class BaseMenu:
    def __init__(self, title, db):
        self.title = title
        self.db = db
        self.selected_entry = ""

    def show(self):
        self.selected_entry = TerminalMenu(
            [entry.item for entry in self.Entry],
            title=self.title,
            clear_screen=True
        ).show()

    def running(self):
        return self.selected_entry != self.Entry.EXIT.num

    def loop(self):
        while self.running():
            self.show()
            self.handle()
