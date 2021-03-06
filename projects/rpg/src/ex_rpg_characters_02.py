import copy
from pprint import pprint
from abc import ABCMeta, abstractmethod


class ActorExistsException(Exception):
    pass


class Actor(metaclass=ABCMeta):
    actors = {}

    def __init__(self, name_, type, health, power):
        if name_ in self.__class__.actors:
            raise ActorExistsException
        self.type_actor = None
        self._name = name_
        self.__class__.actors[name_] = self
        self.type = type
        self.health = health
        self.power = power

    def __str__(self):
        return (f"name: {self.name!r}, "
                f"type: {self.type!r}, "
                f"health: {self.health!r}, "
                f"power: {self.power!r}")

    def  __repr__(self):
        return (f"{self.type_actor}("
                f"{self.name!r}, "
                f"{self.type!r}, "
                f"{self.health!r}, "
                f"{self.power!r})")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v):
        if v in Actor.actors:
            raise ActorExistsException 
        Actor.actors[v] = Actor.actors.pop(self._name)
        self._name = v

    def copy(self, v):
        if v in self.actors:
            raise ActorExistsException
        cp = copy.deepcopy(self)
        cp._name = v
        Actor.actors[v] = cp
        return cp

    @abstractmethod
    def greet(self):
        pass


class Npc(Actor):
    npcs = {}

    def __init__(self, name, type, health, power):
        super().__init__(name, type, health, power)
        self.__class__.npcs[name] = self
        self.type_actor = 'Npc'

    @property
    def name(self):
        return super().name

    @name.setter
    def name(self, v):
        if v == self._name:
            return
        old_name = self._name
        super(Npc, self.__class__).name.fset(self, v)
        Npc.npcs[v] = Npc.npcs.pop(old_name)

    def copy(self, v):
        Npc.npcs[v] = super().copy(v)
        return Npc.npcs[v]

    def greet(self):
        print('Hello!')


class Pc(Actor):
    pcs = {}

    def __init__(self, name, type, health, power):
        super().__init__(name, type, health, power)
        self.__class__.pcs[name] = self
        self.type_actor = 'Pc'

    @property
    def name(self):
        return super().name

    @name.setter
    def name(self, v):
        if v == self._name:
            return
        old_name = self._name
        super(Pc, self.__class__).name.fset(self, v)
        Pc.pcs[v] = Pc.pcs.pop(old_name)

    def copy(self, v):
        Pc.pcs[v] = super().copy(v)
        return Pc.pcs[v]

    def greet(self):
        print('Hi!')


def main():
    p1 = Pc("P1", "rider", 50, 20)
    p2 = Pc("P2", "rider", 35, 45)
    p3 = Pc("P3", "rider", 67, 33)
    baragorn = Npc("Baragorn", "fighter", 100, 20)
    npc_def = [
        ("Aragorn", "rider", 100, 20),
        ("Gandalf", "mage", 110, 520),
        ("Legolas", "thief", 110, 520),
        ]

    some_npcs = [Npc(*npc) for npc in npc_def]

    print("Baragon:")
    pprint(baragorn)
    print("\np1:")
    pprint(p1)
    print("\np2:")
    pprint(p2)
    print("\np3:")
    pprint(p3)
    print("\nsome_npcs:")
    pprint(some_npcs)

    print("\nActors:")
    pprint(Actor.actors)
    print("\nNpcs:")
    pprint(Npc.npcs)
    print("\nPcs:")
    pprint(Pc.pcs)


if __name__ == "__main__":
    main()
