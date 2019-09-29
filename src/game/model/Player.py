class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.current_cards = []
        self.money = 100

    def __str__(self):
        return f'name : {self.name}, score : {self.score}, ' \
               f'current_cards : {[card.face_value for card in self.current_cards]} '

    def collect_card(self, new_card):
        self.current_cards.append(new_card)
        self.score += new_card.face_value

    def prepare_for_new_round(self):
        self.score = 0
        self.current_cards = []
