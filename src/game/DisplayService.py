from tkinter import *
from tkinter import messagebox
import time


class DisplayService:

    def __init__(self, player, dealer, root, deck_service):
        self.player = player
        self.dealer = dealer
        self.image_to_open = None
        self.top = root
        self.deck_service = deck_service
        self.active_player = player
        self.canvas = None

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
        self.show_dealer_cards(canvas, False)

        # Player
        print(self.player)
        self.show_player_cards(canvas)

        hit_button = Button(self.top, text="Hit", command=self.hit, anchor=W)
        hit_button.configure(width=5, activebackground="#33B5E5", relief=FLAT)
        canvas.create_window(450, 300, anchor=NW, window=hit_button)

        stay_button = Button(self.top, text="Stay", command=self.stay, anchor=W)
        stay_button.configure(width=7, activebackground="#33B5E5", relief=FLAT)
        canvas.create_window(500, 300, anchor=NW, window=stay_button)

        canvas.pack()
        self.canvas = canvas
        self.top.mainloop()

    def show_player_cards(self, canvas):
        print(self.player)
        player_spacing = 25
        start = 520
        for position, player_card in enumerate(self.player.current_cards, start=0):
            canvas.create_image(start + (position * player_spacing), (400 - (position * 9)), anchor=NE,
                                image=player_card.get_card_image())

    def show_dealer_cards(self, canvas, delete_old):
        print(self.dealer)
        player_spacing = 25
        start = 520
        for position, dealer_card in enumerate(self.dealer.current_cards, start=0):
            if not dealer_card.visible:
                self.image_to_open = canvas.create_image(start + (position * player_spacing), (50 - (position * 9)),
                                                         anchor=NE,
                                                         image=dealer_card.get_card_image())
            else:
                if delete_old:
                    canvas.itemconfig(self.image_to_open, image=dealer_card.get_card_image())
                else:
                    canvas.create_image(start + (position * player_spacing), (50 - (position * 9)), anchor=NE,
                                        image=dealer_card.get_card_image())

    def hit(self):
        new_card = self.deck_service.draw_card()
        new_card.visible = True
        self.player.collect_card(new_card)
        self.show_player_cards(self.canvas)
        self.inspect_result()
        self.play_dealer_move()

    def stay(self):
        self.play_dealer_move()

    def play_dealer_move(self):
        time.sleep(2)
        move_complete = False
        for card in self.dealer.current_cards:
            if not card.visible:
                card.visible = True
                self.dealer.score += card.face_value
                self.show_dealer_cards(self.canvas, True)
                move_complete = True
                break

        if not move_complete:
            new_card = self.deck_service.draw_card()
            new_card.visible = True
            self.dealer.collect_card(new_card)
            self.show_dealer_cards(self.canvas, False)
            self.inspect_result()

        self.inspect_result()

    def inspect_result(self):
        if self.player.score > 21 and self.dealer.score > 21:
            messagebox.showinfo("Result", "Tie", parent=self.top)
        elif self.player.score > 21:
            messagebox.showinfo("Result", "Dealer Wins !!", parent=self.top)
        elif self.dealer.score > 21:
            messagebox.showinfo("Result", "Player Wins !!", parent=self.top)
