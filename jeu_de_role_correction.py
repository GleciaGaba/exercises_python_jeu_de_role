from random import random, randint


class Player:
    def __init__(self, name: str, health: int = 50, number_of_flasks: int =3):
        self.name = name
        self.health = health
        self.number_of_flasks = number_of_flasks

    def __str__(self):
        return f"{self.name} ({self.health} points de vie)"

    @property
    def damage(self):
        return randint(1, 10)

    @damage.setter
    def damage(self, value):
        raise ValueError("Vous ne pouvez pas modifier les points de dommage")

    def attack(self, enemy: "Player") -> int:
        damage_inflicted = self.damage
        enemy.health -= damage_inflicted
        print(f"{self.name} avez infligé {damage_inflicted} points de dégats à {enemy.name}")
        return damage_inflicted

    def take_flask(self) -> bool:
        if not self.number_of_flasks:
            print("Vous ne pouvez pas prendre de potion")
            return False
        flask_health = randint(5, 50)
        self.health += flask_health
        print(f"{self.name} a récupéré {flask_health} points de vie.")
        return True


def _show_instructions(player: Player, enemy: Player):
    print("Bienvenu sur le jeu di terminal")
    print(f"Vous êtes le {player} et voici le nombre de vos points de vie: {player.health}")
    print(
        f"Vous allez devoir vous battre face à votre adversaire le {enemy} et ses points de vie sont: {enemy.health}")
    print("Voici les instructions : ")
    print("Les dégâts de vos attaques vont de 1 à 10, tandis que votre adversaire peut vous infliger des dégâts "
          "allant de 1 à 15.\n"
          "Vous avez droit à 3 potions pour régenerer votre santé. Mais à chaque usage de votre potion votre "
          "adversaire peut vous attaquer\n"
          "et vous infligez de dégâts mais vous ne pouvez pas l'attaquer.")
    print("Nous pouvons commencer la partie : ")


def _create_players() -> [Player, Player]:
    player_01_name = input("Entrez le nom du premier joueur : ")
    player_02_name = input("Entrez le nom de votre adversaire : ")
    return Player(name=player_01_name), Player(name=player_02_name, number_of_flasks=0)


def _start_game(player, enemy):
    skip_turn = False
    # Tant que le joueur 1 a des points de vie et que l'ennemi a des points de vie on boucle
    while player.health >= 0 and enemy.health >= 0:
        if skip_turn:
            print("Vous passez votre tour")
            enemy.attack(player)
            skip_turn = False
            continue

        action = input("Quelle est votre action(1 /2) : ")
        if action == "1":
            #  On attaque
            player.attack(enemy)
        elif action == "2":
            if player.take_flask():
                # passer in tour
                skip_turn = True

        # Attaque de l'ennemi
        enemy.attack(player)
        print(player)
        print(enemy)

    print(f"{player.name if player.health > 0 else enemy.name} a gagné")


def start(show_instructions=True):
    player, enemy = _create_players()
    if show_instructions:
        _show_instructions(player, enemy)
    _start_game(player, enemy)


def main():
    start()


if __name__ == '__main__':
    start()
