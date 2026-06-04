# ui.py — Person A owns this
# Everything the player sees goes through here

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title="PLAYGRID"):
    print("=" * 50)
    print(f"  {title}")
    print("=" * 50)

def show_player_stats(player):
    print(f"\n[ {player.name} | {player.player_class} | Lvl {player.level} ]")
    print(f"  HP   : {player.hp}/{player.max_hp}")
    print(f"  MP   : {player.mp}/{player.max_mp}")
    print(f"  ATK  : {player.atk}   DEF: {player.def_stat}")
    print(f"  XP   : {player.xp}/{player.xp_next}")
    print(f"  Gold : {player.gold}")

def show_room(room, neighbors, dungeon_map):
    print(f"\n--- {room['name'].upper()} (Room {room['id']}) ---")
    print(f"  Type: {room['type']}")
    print(f"  Connected to:")
    for nid in neighbors:
        n = dungeon_map.get_room(nid)
        print(f"    [{nid}] {n['name']}")

def show_inventory(player):
    print("\n[ INVENTORY — Linked List ]")
    items = player.inventory.to_list()
    if not items:
        print("  (empty)")
    for i, item in enumerate(items):
        print(f"  {i+1}. {item.name} [{item.item_type}]")
    print(f"  Slots: {player.inventory.size}/{player.inventory.capacity}")

def show_nav_stack(nav_stack, dungeon_map):
    print("\n[ NAV STACK ]")
    history = nav_stack.history()
    for i, rid in enumerate(reversed(history)):
        room = dungeon_map.get_room(rid)
        prefix = ">> " if i == 0 else "   "
        print(f"  {prefix}{room['name']}")

def show_battle_start(monster):
    print(f"\n  BATTLE: {monster.name} appears!")
    print(f"  HP: {monster.hp}/{monster.max_hp}")
    print(f"  ATK: {monster.atk}")
    print(f"  Priority: {monster.priority}")

def show_battle_result(attacker, defender, damage):
    print(f"  {attacker} hits {defender} for {damage} damage!")

def show_message(msg, style="info"):
    icons = {
        "info"  : "->",
        "ok"    : "OK",
        "warn"  : "!!",
        "error" : "XX",
        "loot"  : "**"
    }
    icon = icons.get(style, "->")
    print(f"\n  [{icon}] {msg}")

def show_game_over(score):
    print("\n" + "=" * 50)
    print("  GAME OVER")
    print(f"  Final Score: {score}")
    print("=" * 50)

def show_victory():
    print("\n" + "=" * 50)
    print("  YOU WIN — BOSS DEFEATED!")
    print("  [Process EXIT_SUCCESS]")
    print("=" * 50)

def show_actions(room_type, in_battle=False):
    print("\n  ACTIONS:")
    if in_battle:
        print("  [1] Basic Attack")
        print("  [2] Use Skill")
        print("  [3] Use Item")
        print("  [4] Run Away")
    else:
        print("  [M] Move to room")
        print("  [B] Go back")
        print("  [I] Inventory")
        print("  [S] Stats")
        if room_type == "shop":
            print("  [Y] Buy item")
        print("  [Q] Quit")