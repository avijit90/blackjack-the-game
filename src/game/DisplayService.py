from tkinter import *


class DisplayService:

    def __init__(self, player, dealer, root):
        self.player = player
        self.dealer = dealer
        self.displayed_cards = {}
        self.top = root

    def display_table(self, deck):
        canvas = Canvas(self.top, bg="green", height=600, width=1100)

        # Available deck
        start = 200
        end = 250
        deck_spacing = ((end - start) // (len(deck) - 4))

        for position, card in enumerate(deck, start=1):
            canvas.create_image(200 + (deck_spacing * position), 250, anchor=NE, image=card.get_card_image())

        # Dealer
        print(self.dealer)
        player_spacing = 95
        start = 620
        for position, dealer_card in enumerate(self.dealer.current_cards, start=0):
            canvas.create_image(start - (position * player_spacing), 50, anchor=NE, image=dealer_card.get_card_image())

        # Player
        print(self.player)
        for position, player_card in enumerate(self.player.current_cards, start=0):
            canvas.create_image(start - (position * player_spacing), 400, anchor=NE, image=player_card.get_card_image())

        canvas.pack()
        self.top.mainloop()
