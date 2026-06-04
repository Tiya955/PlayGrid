# navigation.py — Person A owns this
# DSA: Stack — navigation history and backtracking

class NavigationStack:
    def __init__(self):
        self._stack = []

    def push(self, room_id):
        self._stack.append(room_id)

    def pop(self):
        if len(self._stack) > 1:
            return self._stack.pop()
        return None

    def peek(self):
        if self._stack:
            return self._stack[-1]
        return None

    def history(self):
        return list(self._stack)

    def size(self):
        return len(self._stack)


def move_player(current_room, destination, dungeon_map, nav_stack, player):
    if not dungeon_map.is_valid_move(current_room, destination):
        return False, "Those rooms are not connected."

    if dungeon_map.is_locked(destination, player):
        return False, "Boss room is LOCKED. Find the Boss Key first. [Semaphore]"

    nav_stack.push(destination)
    room = dungeon_map.get_room(destination)
    return True, f"Moved to: {room['name']}"


def go_back(nav_stack, dungeon_map):
    nav_stack.pop()
    prev = nav_stack.peek()
    if prev is None:
        nav_stack.push(0)
        return 0, "Already at the start."
    room = dungeon_map.get_room(prev)
    return prev, f"Backtracked to: {room['name']} [Stack POP]"