class Players:
    def __init__(self):
        self.players = {1: "X", 2: "O"}
        self.turn = 0

    def cycle_char(self, value):
        char_values = list(self.players.values())

        if value == char_values[0]:
            value = char_values[1]
        elif value == char_values[1]:
            value = char_values[0]

        return value

    def cycle_player(self, value):

        player_value = list(self.players.keys())

        if value == player_value[0]:
            value = player_value[1]
        elif value == player_value[1]:
            value = player_value[0]

        return value
