from tkinter import Tk

from DisplayService import DisplayService
from Player import Player


class AppRunner:

    def __init__(self):
        self.display_service = None


def execute():
    root = Tk()
    display_service = DisplayService(root, Player('Player'), Player('Dealer'))
    display_service.run_game(False)


if __name__ == '__main__':
    execute()
