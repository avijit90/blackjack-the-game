from DisplayService import DisplayService
from Player import Player
from src.game.InputService import InputService


class AppRunner:

    def __init__(self):
        self.display_service = None
        self.input_service = None
        self.human = None
        self.dealer = None


def execute():
    input_service = InputService()
    human = Player(input_service.get_player_name())
    dealer = Player('Dealer')
    display_service = DisplayService(human, dealer)
    display_service.display_table()


if __name__ == '__main__':
    execute()
