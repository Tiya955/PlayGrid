# combat_controller.py — Person A owns this
# Controls fight sequence — calls B's logic, A controls the flow

from ui import (show_battle_start, show_battle_result,
                show_message, show_player_stats, show_actions)

def start_combat(player, monster):
    show_battle_start(monster)

    while player.hp > 0 and monster.hp > 0:
        show_player_stats(player)
        print(f"\n  Enemy: {monster.name} "
              f"HP {monster.hp}/{monster.max_hp}")
        show_actions(None, in_battle=True)

        choice = input("\n  > ").strip().lower()

        if choice == "1":
            dmg = player.attack(monster)
            show_battle_result(player.name, monster.name, dmg)

        elif choice == "2":
            print("  Your skills:", player.skills)
            skill = input("  Skill name: ").strip()
            result = player.use_skill(skill, monster)
            if result == -1:
                show_message("Not enough MP!", "warn")
                continue
            show_battle_result(
                f"{player.name} ({skill})", monster.name, result
            )

        elif choice == "3":
            items = player.inventory.to_list()
            if not items:
                show_message("No items!", "warn")
                continue
            for i, it in enumerate(items):
                print(f"  [{i+1}] {it.name}")
            idx = input("  Choose number: ").strip()
            if idx.isdigit() and 1 <= int(idx) <= len(items):
                item = items[int(idx) - 1]
                msg = item.use(player)
                player.inventory.remove(item.name)
                show_message(f"Used {item.name}: {msg}", "ok")

        elif choice == "4":
            show_message("You fled!", "warn")
            return "fled"

        else:
            show_message("Invalid input.", "error")
            continue

        # Enemy turn
        if monster.hp > 0:
            dmg = monster.attack(player)
            show_battle_result(monster.name, player.name, dmg)

    if player.hp <= 0:
        show_message("You died. [Process SIGKILL]", "error")
        return "lose"

    show_message(
        f"{monster.name} defeated! "
        f"+{monster.xp_reward} XP  "
        f"+{monster.gold_reward} Gold", "loot"
    )
    leveled = player.gain_xp(monster.xp_reward)
    player.gain_gold(monster.gold_reward)
    if leveled:
        show_message(f"LEVEL UP -> {player.level}!", "ok")
    return "win"