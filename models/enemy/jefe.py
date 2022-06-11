from models.enemy.enemy import Enemy


class Jefe(Enemy):

    def __init__(self):
        self.hp: int = 0
        self.mp: int = 0
        self.st: int = 0
        self.posx: int = 0
        self.posy: int = 0

    def saltar(self, txt: str):
        pass

    def super_ataque(self, txt: str):
        pass

    def avanzar(self, txt: str):
        pass

    def retroceder(self, txt: str):
        pass

    def atacar(self, txt: str):
        pass
    