from tkinter import Tk

from DeckService import DeckService
from DisplayService import DisplayService
from InputService import InputService
from Player import Player


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
    root = Tk()
    display_service = DisplayService(human, dealer, root)
    deck_service = DeckService()
    deck_service.build_deck()
    dealer.current_cards = deck_service.draw_dealer_initial_cards()
    human.current_cards = deck_service.draw_dealer_initial_cards()
    display_service.display_table(deck_service.deck)


if __name__ == '__main__':
    execute()
