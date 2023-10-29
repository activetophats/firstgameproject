import random
from Food import*
class Person:
    def __init__(self,):
        self.energy=100
        self.health=60
        self.inventory = {}
        self.coordinate=[0,0]
    def eat(self, food):
        pass
    def run(self, hours, direction):

        self.energy=self.energy-10*hours
        if self.energy<0:
            print("You Died.")
            return False
        return True
    def sleep(self, hours):
        if hours>12:
            print("You slept too long.")
            self.energy=self.energy+1*hours
            print("You've slept for" + hours + "hours. You've gained" + str(1*hours) + "energy!")
        else:
            self.energy=self.energy+5*hours
            print("You've slept for" + str(hours) + "hours. You've gained"+ str(5*hours) +  "energy!")
    def stats(self,):
        print("Your current energy is " + str(self.energy))
        print("Your current height is " + str(self.height))
    def gathering(self, hours,) :
        pass
