import enum


class RoleType(enum.Enum):
    WHITE = 'WHITE'
    GREY = 'GREY'
    BLACK = 'BLACK'


class Role:
    pass


class Doctor(Role):
    def __init__(self):
        self.role_type = RoleType.WHITE

    def save(self):
        pass


class Citizen(Role):
    def __init__(self):
        self.role_type = RoleType.WHITE


class Mafia(Role):
    def __init__(self):
        self.role_type = RoleType.BLACK
    def kill(self):
        pass


class Don(Mafia):
    pass


class Joker(Role):
    def __init__(self):
        self.role_type = RoleType.GREY


class Natasha(Role):
    def __init__(self):
        self.role_type = RoleType.GREY
    def mute(self):
        pass


class Priest(Role):
    def __init__(self):
        self.role_type = RoleType.WHITE
    def unmute(self):
        pass


class Thief(Role):
    def __init__(self):
        self.role_type = RoleType.GREY
    def steal(self):
        pass


class Sniper(Role):
    def __init__(self):
        self.role_type = RoleType.WHITE
    def shoot(self):
        pass
