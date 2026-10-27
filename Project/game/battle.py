class Battle:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def start(self):
        print("\n--------------------------------------------")
        print(f"A wild {self.enemy.name} appears!")
        print("--------------------------------------------")

        while self.hero.is_alive() and self.enemy.is_alive():
            print(
                "\n" + self.hero.show_status()
                + "   |   " + self.enemy.show_status()
            )

            print("1 - Attack")
            print("2 - Special move")
            print("3 - Use potion")

            choice = input("Choose (1-3): ")

            if choice == "1":
                print(self.hero.attack(self.enemy))

            elif choice == "2":
                if self.hero.can_use_special():
                    print(self.hero.special_move(self.enemy))
                else:
                    print("You cannot use your special move yet!")
                    continue

            elif choice == "3":
                if self.hero.potions == 0:
                    print("No potions left!")
                    continue

                print(self.hero.use_potion())

            else:
                print("Invalid choice.")
                continue

            if self.enemy.is_alive():
                print(self.enemy.take_turn(self.hero))

        return self.hero.is_alive()
