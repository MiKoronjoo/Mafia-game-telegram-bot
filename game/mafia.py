import random
from game.roles import *

roles = {4: [Doctor, Mafia, Citizen, Citizen],
         5: [Doctor, Mafia, Citizen, Citizen, Citizen],
         6: [Doctor, Mafia, Mafia, Citizen, Citizen, Citizen],
         7: [Doctor, Mafia, Mafia, Citizen, Citizen, Citizen, Citizen],
         8: [Doctor, Mafia, Mafia, Mafia, Citizen, Citizen, Citizen, Citizen],
         9: [Doctor, Mafia, Mafia, Mafia, Citizen, Citizen, Citizen, Citizen, Citizen],
         10: [Doctor, Mafia, Mafia, Mafia, Citizen, Citizen, Citizen, Citizen, Citizen, Citizen],
         11: [Doctor, Mafia, Mafia, Mafia, Mafia, Citizen, Citizen, Citizen, Citizen, Citizen, Citizen]}


class Time(enum.Enum):
    DAY = 'DAY'
    VOTING = 'VOTING'
    NIGHT = 'NIGHT'


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

    def send_public_message(self, message):
        print(message)

    def send_message(self, message, chat_id):
        print('To %d: %s' % (chat_id, message))


class Game:
    def __init__(self, group_name, group_id):
        self.group_name = group_name
        self.group_id = group_id
        self.players = []
        self.manager = None
        self.time = Time.DAY

    def join_player(self, player):
        self.players.append(player)
        self.manager.send_public_message(player.name + ' joined!')

    def set_roles(self):
        no_role_players = list(range(len(self.players)))
        for TheRole in roles[len(self.players)]:
            i = random.choice(no_role_players)
            self.players[i].role = TheRole()
            self.manager.send_message('You are ' + self.players[i].role.role, self.players[i].id)
            no_role_players.remove(i)


def main():
    ###### TEST ######
    game = Game('group_name', 123456)
    manager = Manager(game)
    game.manager = manager

    manager.send_public_message('Join the game!')
    game.join_player(Player('a', 11))
    game.join_player(Player('b', 12))
    game.join_player(Player('c', 13))
    game.join_player(Player('d', 14))
    game.join_player(Player('e', 15))

    game.set_roles()

    ##################


if __name__ == '__main__':
    main()
