from Pokemon import *
import math
import random

class Trainer:
    def __init__(self,name,pokemon_names):
        self.name=name
        self.pokemon=[]
        self.opponent=0

        for i in pokemon_names:
            pokemon_i=Pokemon(i)
            self.pokemon.append(pokemon_i)

    def print_mons(self):
        print("\nTrainer name is",self.name)
        for i in self.pokemon:
            i.nat_b()
            i.calc_stats()
            i.displaying()

    def fight(self,Player):
        self.opponent=Player
        print("\nYou are fighting against",self.name)
        print("They sent out",self.pokemon[0].name)

        self.pokemon[0].nat_b()
        self.pokemon[0].calc_stats()

        print("\nYou sent out",self.opponent.pokemon[0].name)

        print("Your",self.opponent.pokemon[0].name,"is at",self.opponent.pokemon[0].hp,"HP")
        print("Your",self.pokemon[0].name,"is at",self.pokemon[0].hp,"HP")

        print("\nYour moves are:")
        for i in self.opponent.pokemon[0].moves:
            print(i.name)
        
        move_chosen=input("Which Move would you like to Use? ")

        try:
            move_chosen=int(move_chosen)
            move_used=self.opponent.pokemon[0].moves[move_chosen-1].name
            print("\nYour",self.opponent.pokemon[0].name,"used",move_used)

            # damage_p=math.ceil(self.opponent.pokemon[0].moves[move_chosen-1].power*
            #                    ((self.opponent.pokemon[0].att/self.pokemon[0].defe)/25)+1
            #                    )
            # print(damage_p)

        except ValueError as ve:
            print("Invalid Move")
