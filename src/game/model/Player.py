class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.current_cards = []

    def __str__(self):
        print(f'name : {self.name}, score : {self.score}, current_cards : {self.current_cards} ')
