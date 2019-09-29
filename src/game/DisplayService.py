from tkinter import *
from tkinter import messagebox

from DeckService import DeckService


class DisplayService:

    def __init__(self, root, player, dealer):
        self.player = player
        self.dealer = dealer
        self.image_to_open = None
        self.top = root
        self.deck_service = None
        self.canvas = None
        self.result = False

    def display_table(self, deck, reset_game):

        self.result = False

        if not reset_game:
            canvas = Canvas(self.top, bg="green", height=600, width=950)
        else:
            canvas = self.canvas

        # Available deck
        start = 200
        end = 250
        deck_spacing = ((end - start) // (len(deck) - 4))

        if reset_game:
            canvas.delete("dealer_score_tag")
            canvas.delete("player_score_tag")
            canvas.delete("clear_on_Reset")

        for position, card in enumerate(deck, start=1):
            canvas.create_image(200 + (deck_spacing * position), 250, anchor=NE, image=card.get_card_image(),
                                tag='clear_on_Reset')

        # Dealer
        self.show_dealer_cards(canvas, False)

        # Player
        self.show_player_cards(canvas)

        hit_button = Button(self.top, text="Hit", command=self.hit, anchor=W)
        hit_button.configure(width=5, activebackground="#33B5E5", relief=FLAT)
        canvas.create_window(400, 300, anchor=NW, window=hit_button)
        stay_button = Button(self.top, text="Stay", command=self.stay, anchor=W)
        stay_button.configure(width=7, activebackground="#33B5E5", relief=FLAT)
        canvas.create_window(450, 300, anchor=NW, window=stay_button)
        reset_button = Button(self.top, text="Play Again", command=self.reset_game, anchor=W)
        reset_button.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        canvas.create_window(515, 300, anchor=NW, window=reset_button)

        canvas.create_text(800, 50, fill="cyan", font="Times 20 italic bold",
                           text="Dealer Score", tag='clear_on_Reset')

        canvas.create_text(800, 400, fill="white", font="Times 20 italic bold",
                           text="Player Score", tag='clear_on_Reset')

        canvas.pack()

        if not reset_game:
            self.top.title('Blackjack')
            self.canvas = canvas
            self.top.mainloop()
        else:
            self.canvas = canvas

    def show_player_cards(self, canvas):
        print(self.player)
        player_spacing = 25
        start = 520

        canvas.delete("player_score_tag")
        canvas.create_text(800, 430, fill="white", font="Times 20 italic bold", text=self.player.score,
                           tag="player_score_tag")

        for position, player_card in enumerate(self.player.current_cards, start=0):
            canvas.create_image(start + (position * player_spacing), (400 - (position * 9)), anchor=NE,
                                image=player_card.get_card_image(), tag='clear_on_Reset')

    def show_dealer_cards(self, canvas, delete_old):
        print(self.dealer)
        player_spacing = 25
        start = 520

        canvas.delete("dealer_score_tag")
        canvas.create_text(800, 80, fill="cyan", font="Times 20 italic bold", text=self.dealer.score,
                           tag="dealer_score_tag")

        for position, dealer_card in enumerate(self.dealer.current_cards, start=0):
            if not dealer_card.visible:
                self.image_to_open = canvas.create_image(start + (position * player_spacing), (50 - (position * 9)),
                                                         anchor=NE,
                                                         image=dealer_card.get_card_image(), tag='test_image')
            else:
                if delete_old:
                    canvas.itemconfig(self.image_to_open, image=dealer_card.get_card_image())
                else:
                    canvas.create_image(start + (position * player_spacing), (50 - (position * 9)), anchor=NE,
                                        image=dealer_card.get_card_image(), tag='test_image')

    def hit(self):
        if self.result:
            return

        new_card = self.deck_service.draw_card()
        new_card.visible = True
        self.player.collect_card(new_card)
        self.show_player_cards(self.canvas)
        self.inspect_result()

    def stay(self):
        if self.result:
            return

        self.play_dealer_move()

    def play_dealer_move(self):
        self.inspect_result()

        if self.result:
            return

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

    def inspect_result(self):
        if self.result:
            return

        if self.player.score == 21 and self.dealer.score == 21:
            self.result = True
            messagebox.showinfo("Result", "Tie", parent=self.top)
        elif self.player.score > 21:
            self.result = True
            messagebox.showinfo("Result", "Dealer Wins !!", parent=self.top)
        elif self.dealer.score > 21:
            self.result = True
            messagebox.showinfo("Result", "Player Wins !!", parent=self.top)
        elif 17 < self.dealer.score < 21 and 21 >= self.player.score > self.dealer.score:
            self.result = True
            messagebox.showinfo("Result", "Player Wins !!", parent=self.top)

    def run_game(self, reset_game):
        self.deck_service = DeckService()
        self.deck_service.build_deck()
        self.dealer.current_cards = self.deck_service.draw_dealer_cards(self.dealer)
        self.player.current_cards = self.deck_service.draw_player_cards(self.player)
        self.display_table(self.deck_service.deck, reset_game)

    def reset_game(self):
        print('<<---------------<< Resetting Game >>------------------>>')
        self.run_game(True)
