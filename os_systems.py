class Semaphore:
    def __init__(self, value=1):
        self._value = value
        self._locked = value == 0

    def acquire(self, key=False):
        if self._locked:
            print("SEMAPHORE: Boss room is locked! You need a key.")
            return False
        if key:
            self._locked = True
            print("SEMAPHORE: Room acquired, locking behind you.")
        return True

    def release(self):
        self._locked = False
        print("SEMAPHORE: Boss room unlocked!")


class DeadlockDemo:
    def __init__(self):
        self.resource_a = "Sword"
        self.resource_b = "Shield"
        self.player1_holds = None
        self.player2_holds = None

    def simulate(self):
        print("\n-- Deadlock Demo --")
        self.player1_holds = self.resource_a
        self.player2_holds = self.resource_b
        print(f"Player1 holds {self.player1_holds}, wants {self.resource_b}")
        print(f"Player2 holds {self.player2_holds}, wants {self.resource_a}")
        print("Neither can proceed — DEADLOCK!")

s = Semaphore(0)
s.acquire()
s.release()
s.acquire(key=True)

d = DeadlockDemo()
d.simulate()