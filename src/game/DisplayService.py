from tkinter import *


class DisplayService:

    def __init__(self, player, dealer, root):
        self.player = player
        self.dealer = dealer
        self.displayed_cards = {}
        self.top = root

    def display_table(self, deck):
        canvas = Canvas(self.top, bg="green", height=600, width=1100)

        closed_card = PhotoImage(file="../../resources/90X150/card_back.png")
        face_card = PhotoImage(file="../../resources/90X150/2_of_clubs.png")

        # Available deck
        start = 200
        end = 250
        spacing = ((end - start) // (len(deck) - 4))

        for position, card in enumerate(deck, start=1):
            canvas.create_image(200 + (spacing * position), 250, anchor=NE, image=card.get_card_image())

        # Dealer
        print(self.dealer)
        spacing = 95
        start = 620
        for position, dealer_card in enumerate(self.dealer.current_cards, start=0):
            canvas.create_image(start - (position * spacing), 50, anchor=NE, image=dealer_card.getcard_image())

        # canvas.create_image(400 + 220, 50, anchor=NE, image=closed_card)
        # canvas.create_image(525, 50, anchor=NE, image=face_card)

        # Player
        self.player
        canvas.create_image(620, 400, anchor=NE, image=face_card)
        canvas.create_image(525, 400, anchor=NE, image=face_card)

        canvas.pack()

        self.top.mainloop()
