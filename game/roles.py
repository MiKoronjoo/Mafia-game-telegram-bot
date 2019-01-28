import enum


class RoleType(enum.Enum):
    WHITE = 'WHITE'
    GREY = 'GREY'
    BLACK = 'BLACK'


class Role:
    role = 'role'


class Doctor(Role):
    role = 'doctor'
    role_type = RoleType.WHITE

    def __init__(self):
        pass

    def save(self):
        pass


class Citizen(Role):
    role = 'citizen'
    role_type = RoleType.WHITE

    def __init__(self):
        pass


class Mafia(Role):
    role = 'mafia'
    role_type = RoleType.BLACK

    def __init__(self):
        pass

    def kill(self):
        pass


class Don(Mafia):
    role = 'don'


class Joker(Role):
    role = 'joker'
    role_type = RoleType.GREY

    def __init__(self):
        pass


class Natasha(Role):
    role = 'natasha'
    role_type = RoleType.GREY

    def __init__(self):
        pass

    def mute(self):
        pass


class Priest(Role):
    role = 'priest'
    role_type = RoleType.WHITE

    def __init__(self):
        pass

    def unmute(self):
        pass


class Thief(Role):
    role = 'thief'
    role_type = RoleType.GREY

    def __init__(self):
        pass

    def steal(self):
        pass


class Sniper(Role):
    role = 'sniper'
    role_type = RoleType.WHITE

    def __init__(self):
        pass

    def shoot(self):
        pass
