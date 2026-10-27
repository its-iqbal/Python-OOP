from characters.heroes import Warrior, Mage, Paladin
from characters.enemies import Enemy, Dragon
from characters.character import Character
from game.battle import Battle


def choose_hero():
    print("\nChoose your hero:")
    print("1 - Warrior (strong, gains rage when attacking)")
    print("2 - Mage (uses mana for powerful Fireball)")
    print("3 - Paladin (a Warrior and a Mage combined)")

    choice = input("Choose (1-3): ")

    while choice not in ["1", "2", "3"]:
        choice = input("Invalid. Choose (1-3): ")

    name = input("Enter your hero's name: ")

    if choice == "1":
        return Warrior(name)
    elif choice == "2":
        return Mage(name)
    else:
        return Paladin(name)


def play():
    hero = choose_hero()

    enemies = [
        Enemy("Goblin", 40, 8),
        Enemy("Orc", 65, 10),
        Dragon("Dragon", 100, 12)
    ]

    for enemy in enemies:
        battle = Battle(hero, enemy)

        if battle.start():
            print(f"\nYou defeated the {enemy.name}!")
            hero.heal(40)
            print("You rest a little and recover 40 HP.")
        else:
            print(
                f"\n{hero.name} was defeated by "
                f"the {enemy.name}. GAME OVER."
            )
            break

    else:
        print(
            f"\n*** CONGRATULATIONS {hero.name}! "
            "You defeated all enemies! ***"
        )

    print(
        f"Characters created so far: "
        f"{Character.total_characters()}"
    )


def show_mro():
    print("\nMRO of Paladin (method search order):")

    for cls in Paladin.__mro__:
        print("  ->", cls.__name__)


def main():
    while True:
        print("\n===== TEXT RPG : THE BATTLE ARENA =====")
        print("1 - Play")
        print("2 - Show Paladin MRO")
        print("3 - Exit")

        option = input("Choose (1-3): ")

        if option == "1":
            play()

        elif option == "2":
            show_mro()

        elif option == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
