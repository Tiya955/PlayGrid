# map.py — Person A owns this
# DSA: Graph (adjacency list)

class DungeonMap:
    def __init__(self):
        self.rooms = {}
        self.adjacency = {}
        self._build_map()

    def _build_map(self):
        room_list = [
            {"id": 0, "name": "Start Chamber",  "type": "start"},
            {"id": 1, "name": "Goblin Den",      "type": "battle"},
            {"id": 2, "name": "Dark Tomb",       "type": "battle"},
            {"id": 3, "name": "Alchemy Lab",     "type": "shop"},
            {"id": 4, "name": "Treasure Vault",  "type": "chest"},
            {"id": 5, "name": "Shadow Cave",     "type": "battle"},
            {"id": 6, "name": "Rest Shrine",     "type": "rest"},
            {"id": 7, "name": "Dragon Lair",     "type": "battle"},
            {"id": 8, "name": "Boss Throne",     "type": "boss"},
        ]
        for r in room_list:
            self.rooms[r["id"]] = r
            self.adjacency[r["id"]] = []

        edges = [
            (0, 1), (0, 5),
            (1, 2), (1, 6),
            (2, 3), (2, 7),
            (3, 4),
            (5, 6),
            (6, 7),
            (7, 8),
        ]
        for a, b in edges:
            self.adjacency[a].append(b)
            self.adjacency[b].append(a)

    def get_room(self, room_id):
        return self.rooms.get(room_id)

    def get_neighbors(self, room_id):
        return self.adjacency.get(room_id, [])

    def is_valid_move(self, current_id, destination_id):
        return destination_id in self.adjacency.get(current_id, [])

    def is_locked(self, room_id, player):
        if self.rooms[room_id]["type"] == "boss":
            return not player.inventory.has_item("Boss Key")
        return False