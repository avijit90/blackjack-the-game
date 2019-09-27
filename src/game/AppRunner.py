from tkinter import Tk

from DisplayService import DisplayService


class AppRunner:

    def __init__(self):
        self.display_service = None


def execute():
    root = Tk()
    display_service = DisplayService(root)
    display_service.run_game()


if __name__ == '__main__':
    execute()
