class InputService:

    def __init__(self):
        # self.player = None
        # self.dealer = None
        pass

    @staticmethod
    def get_player_name():
        player_name_input = input("Player, please enter you name\n")
        return player_name_input.title()
