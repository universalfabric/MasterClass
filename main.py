from playerlt import Player
from enemy import Enemy, Troll, VampireKing

mike = Player("Mike")

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

nosferatu = VampireKing("Nosferatu Rex")
nosferatu.speak()


while nosferatu.alive:
        nosferatu.take_damage(20)
        print(nosferatu)
