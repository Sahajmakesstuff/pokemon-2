from Pokemon import *
import math
import random
from typechart import *

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

        done=0
        while done==0:

            print("Your",self.opponent.pokemon[0].name,"is at",self.opponent.pokemon[0].hp,"HP")
            print("Opposing",self.pokemon[0].name,"is at",self.pokemon[0].hp,"HP")

            print("\nYour moves are:")
            for i in self.opponent.pokemon[0].moves:
                print(i.name)
            
            move_chosen=input("Which Move would you like to Use? ")

            try:
                move_chosen=int(move_chosen)
                move_used=self.opponent.pokemon[0].moves[move_chosen-1].name
                print("\nYour",self.opponent.pokemon[0].name,"used",move_used)

                stab_p=1

                if self.opponent.pokemon[0].moves[move_chosen-1].type==self.opponent.pokemon[0].type:
                    stab_p=1.5
                
                crit_dmg_p=1
                crit_var_p=random.randrange(1,17)
                critical_hit=False

                if crit_var_p==10:
                    critical_hit=True
                    crit_dmg_p=1.5
                
                rand_p=random.randrange(8,10)
                rand_p=rand_p/10

                effect_p=1
                super_effective=False
                not_effective=False

                if self.opponent.pokemon[0].moves[move_chosen-1].type in type_chart[self.pokemon[0].type][1]:
                    effect_p=2
                    super_effective=True

                elif self.opponent.pokemon[0].moves[move_chosen-1].type in type_chart[self.pokemon[0].type][0]:
                    effect_p=0.5
                    not_effective=True

                damage_p=math.ceil((((22*self.opponent.pokemon[0].moves[move_chosen-1].power*
                                self.opponent.pokemon[0].att/self.pokemon[0].defe)/25)+2)*
                                stab_p *rand_p *effect_p *crit_dmg_p)

                self.pokemon[0].hp=self.pokemon[0].hp-damage_p

                if super_effective==True:
                    print("The",self.opponent.pokemon[0].moves[move_chosen-1].name,"was super Effective")
                if not_effective==True:
                    print("The",self.opponent.pokemon[0].moves[move_chosen-1].name,"was not very Effective")

                if critical_hit==True:
                    print("The",self.opponent.pokemon[0].moves[move_chosen-1].name,"Was a Critical Hit")

                print("The",self.opponent.pokemon[0].moves[move_chosen-1].name,"did",damage_p,"HP of damage")

                if self.pokemon[0].hp<=0:
                    print(self.pokemon[0].name,"Fainted")
                    done=1
                    break

            except ValueError as ve:
                print("Invalid Move")
        
        if done==1:
            print("You defeated",self.name,"!")

            #comment


