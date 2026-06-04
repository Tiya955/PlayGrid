class Scheduler:
    READY = "READY"
    RUNNING = "RUNNING"
    TERMINATED = "TERMINATED"

    def __init__(self, player, monster):
        self.player = player
        self.monster = monster
        self.player_state = self.READY
        self.monster_state = self.READY

    def run(self):
        print(f"\n⚔ Battle Start: {self.player._name} vs {self.monster._name}")
        turn = 0
        while self.player.is_alive() and self.monster.is_alive():
            turn += 1
            print(f"\n-- Turn {turn} --")
            if turn % 2 != 0:
                self.player_state = self.RUNNING
                print(f"[{self.player_state}] {self.player._name}'s turn")
                self.player.attack(self.monster)
                self.player_state = self.READY
            else:
                self.monster_state = self.RUNNING
                print(f"[{self.monster_state}] {self.monster._name}'s turn")
                self.monster.attack(self.player)
                self.monster_state = self.READY

        if self.player.is_alive():
            self.player_state = self.TERMINATED
            print(f"\n{self.monster._name} defeated!")
        else:
            self.monster_state = self.TERMINATED
            print(f"\n{self.player._name} defeated!")

from entity import Warrior, Monster

w = Warrior("Thor", 100)
m = Monster("Goblin", 50)
s = Scheduler(w, m)
s.run()