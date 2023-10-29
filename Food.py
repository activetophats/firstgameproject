import random
class Fruits:
    def __init__(self, energy, chance, poison_chance):
        self.energy = energy
        self.chance = chance          
        self.is_poison = poison_chance
class Apple(Fruits):
    def __init__(self,  energy, chance, poison_chance):
        super().__init__(energy, chance, poison_chance)
class Cherries(Fruits):
    def __init__(self, energy, chance, poison_chance):
        super().__init__(energy, chance, poison_chance,)
class Bananas(Fruits):
    def __init__(self, energy, chance, poison_chance, health):
        super().__init__(self, energy, chance, poison_chance)
        self.health=health
class Wild:
    def __init__(self,):
        self.wild_fruits=[Apple(5,50,0.05), Cherries(1,20,0.5), Bananas(7,10,0.01,5)]
    def gather (self, hours):
        fruit_chance=[]
        result=[]
        for fruit in self.wild_fruits:
            fruit_chance.append(fruit.chance)
        for hour in range(hours):
            for chance in fruit_chance:
                Wild.random_chance(chance)
    @staticmethod    
    def random_chance(percent):
        return random.randrange(100) < percent
print("")