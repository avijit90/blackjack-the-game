class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.current_cards = []

    def __str__(self):
        return f'name : {self.name}, score : {self.score}, ' \
               f'current_cards : {[card.face_value for card in self.current_cards]} '
