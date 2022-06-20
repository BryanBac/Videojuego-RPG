from abc import ABCMeta, abstractmethod


class Enemy(metaclass=ABCMeta):

    @abstractmethod
    def avanzar(self, txt: str):
        raise NotImplementedError

    @abstractmethod
    def retroceder(self, txt: str):
        raise NotImplementedError

    @abstractmethod
    def atacar(self, txt: str):
        raise NotImplementedError
