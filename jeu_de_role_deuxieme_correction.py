from random import randint

health_player = 50
health_enemy = 50
available_choices = ["1", "2"]
stock_potion = 3
menu = "Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?"
skip_turn = False

while health_player > 0 and health_enemy > 0:

    damage_player = randint(5, 10)
    damage_enemy = randint(5, 15)

    if not skip_turn and ((user_choice := input(menu)) in available_choices):
        if user_choice == "1":
            print(f"Vous avez inflige {damage_player} à votre ennemi.")
            health_enemy -= damage_player

        elif user_choice == "2":
            if stock_potion <= 0:
                print("Vous n'avez plus de potion...")
            else:
                potion_points = randint(15, 50)
                health_player += potion_points
                stock_potion -= 1
                skip_turn = True
                print(f"Vous récupérez {potion_points} points de vie ({stock_potion} potions restantes)")
    elif skip_turn:
        print("Vous passez votre tour")
        skip_turn = False

    else:
        print("Svp faites un choix valide.")
        continue

    print(f"L'ennemi vous a infligé {damage_enemy} points de dommages")
    health_player -= damage_enemy

    print(f"Vous avez {health_player} points")
    print(f"Votre ennemi a {health_enemy}")

if health_enemy <= 0:
    print("Bravo ! \nVous avez gagné ! \nFin du jeu !")
else:
    print("Dommage !\nVous avez perdu.")
