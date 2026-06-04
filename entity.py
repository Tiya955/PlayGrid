from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    def take_damage(self, amount):
        self._hp -= amount

    def is_alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, target):
        pass

class Player(Entity):
    
    def __init__(self, name, hp, level=1):
        super().__init__(name, hp)
        self.level = level

class Warrior(Player):
    def attack(self, target):
        dmg = 15
        target.take_damage(dmg)
        print(f"{self._name} slashes for {dmg} damage!")

class Mage(Player):
    def attack(self, target):
        dmg = 25
        target.take_damage(dmg)
        print(f"{self._name} casts fireball for {dmg} damage!")

class Monster(Entity):
    def __init__(self, name, hp, priority=1):
        super().__init__(name, hp)
        self.priority = priority   # used by priority queue

    def attack(self, target):
        dmg = 10
        target.take_damage(dmg)
        print(f"{self._name} hits for {dmg} damage!")

class BossMonster(Monster):
    def attack(self, target):
        dmg = 30
        target.take_damage(dmg)
        print(f"{self._name} uses BOSS SLAM for {dmg} damage!")

