from random import randint

class Die:
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        number = randint(1,self.sides)
        print(number)

my_die = Die()
for i in range(10):
    my_die.roll_die()

my_die = Die(10)
for i in range(10):
    my_die.roll_die()

my_die = Die(20)
for i in range(10):
    my_die.roll_die()