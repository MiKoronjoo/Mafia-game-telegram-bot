class Role:
    pass


class Doctor(Role):
    def save(self):
        pass


class Citizen(Role):
    pass


class Mafia(Role):
    def kill(self):
        pass


class Don(Mafia):
    pass


class Joker(Role):
    pass


class Natasha(Role):
    def mute(self):
        pass


class Priest(Role):
    def unmute(self):
        pass


class Thief(Role):
    def steal(self):
        pass


class Sniper(Role):
    def shoot(self):
        pass
