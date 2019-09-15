import random

from Card import Card

face_card_img_folder = "../../../resources/90X150/"
card_back_img = "../../../resources/90X150/card_back.png"
card_families = ('clubs', 'diamonds', 'hearts', 'spades')
suite = {'ace': 11, 'jack': 10, 'queen': 10, 'king': 10}
for num in range(2, 11):
    suite[str(num)] = num


class DeckService:

    def __init__(self):
        self.deck = []
        # print(['♡', '♢', '♤', '♧'])

    def build_deck(self):
        for family in card_families:
            for card in suite:
                face_img_path = f'{face_card_img_folder}{card}_of_{family}.png'
                card = Card(suite[card], face_img_path, card_back_img)
                self.deck.append(card)

    def shuffle_deck(self, n):
        for i in range(n):
            r = i + (random.randint(0, 55) % (52 - i))
            tmp = self.deck[i]
            self.deck[i] = self.deck[r]
            self.deck[r] = tmp

    def draw_card(self):
        drawn_card = self.deck.pop()
        return drawn_card