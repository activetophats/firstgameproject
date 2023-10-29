import Person
import math
class Region:
    def __init__(self,rows:int,columns:int,fruit_chance:float, animal_chance:float, zombie_chance:float ,energy_depletion:float, name:str, player:Person):
        self.graph=[] 
        self.fruitP=fruit_chance
        self.animalP=animal_chance
        self.zombieP=zombie_chance
        self.energy_depletion=energy_depletion
        self.names=name
        self.player=player
        self.rows=rows
        self.columns=columns
        self.coordinate=[-1,-1]
        for i in range(rows):
            column = []
            for j in range(columns):
                column.append(0)
            self.graph.append(column)
    def update(self,distance,direction,coordinate = None):
        if coordinate is not None:
            self.coordinate = coordinate

        if direction  == 'left' or direction == 'right':
            self.coordinate[1] += distance
        else:
            self.coordinate[0] += distance
        
        #  travelign up
        if self.coordinate[0]<0:
            return (math.abs(self.coordinate[0]), (0,-1))

        # traveling down
        if self.coordinate[0]>self.rows:
            return (self.rows-self.coordinate[0],(0,1))
        # travlong left
        if self.coordinate[1]<0:
            return (math.abs(self.coordinate[1]),(-1,0))
        # traveling to the right
        if self.coordinate[1]>self.columns:
            return (self.columns-self.coordinate[1],(1,0))
    # def update(self):
# 100% fruits, 100% zombies, 100% animals
# cold - 25% fruits, 0%zombies, 25% animals, 125% faster energy depletion
# hot - 100% animals, 100% zombies, 125% fruits ,125% faster energy depletion
# safe -
player1=Person.Person()
print(player1)
cold = Region(rows = 10, columns = 10,
                fruit_chance=.25,zombie_chance = .10,
                animal_chance = .25, energy_depletion = 0.25,
                name = "cold",player = player1)
hot = Region(rows = 10, columns = 20,
                fruit_chance=1,zombie_chance = 0.20,
                animal_chance = 0.30, energy_depletion = 0.35,
                name = "hot",player = player1)
safe = Region(rows = 10, columns = 10,
                fruit_chance=0.75,zombie_chance = 0.01,
                animal_chance = 0.5, energy_depletion = 20,
                name = "safe",player = player1)
dangerous = Region(rows = 10, coloumns =  10,
                fruit_chance=0.90,zombie_chance = 0.30,
                animal_chance =0.65, energy_depletion = 0.40,
                name = "dangerous",player = player1)
class Graph:
    def __init__(self, player):
        self.graph = [
            [cold,hot],
            [dangerous,safe]]
        self.player = player
        randomVal = random.randint(0,2)

        self.currentRegion = self.graph[randomVal%2][randomVal//2]
    def update(self,distance, direction):

        if direction == "x":
            self.player.coordinate[0] += distance
        else:
            self.player.coordinate[1] += distance