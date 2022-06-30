from models.enemy.enemy import Enemy


class Mob1(Enemy):

    def __init__(self):
        self.hp: int = 0
        self.st: int = 0
        self.posx: int = 0
        self.posy: int = 0

    def avanzar(self, txt: str):
        pass

    def retroceder(self, txt: str):
        pass

    def atacar(self, txt: str):
        pass
