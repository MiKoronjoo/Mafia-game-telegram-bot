class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.role = None

    def vote(self, player):
        pass

    def flee(self):
        pass


class Manager:
    def __init__(self, game):
        self.game = game

    def send_message(self, message):
        pass


class Game:
    def __init__(self, group_name, group_id):
        self.group_name = group_name
        self.group_id = group_id
        self.players = []
        self.manager = None
