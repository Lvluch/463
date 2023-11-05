from Character import Character
from Ninja import Ninja

player1 = Character('Петя')
player2 = Ninja('Вася')

print(player1)
print(player2)

while player1.health > 0 or player2.health > 0:
    player1_dmg = player1.attack(player2)
    player2_dmg = player2.attack(player1)

    print(f'{player1.name} атаковал {player2.name} и нанёс {player1_dmg} урона.')
    print(f'У {player2.name} осталось {player2.health} здоровья.')
    print(f'{player2.name} атаковал {player1.name} и нанёс {player2_dmg} урона.')
    print(f'У {player1.name} осталось {player1.health} здоровья.')
    print()

print(player2)
print(player1)
