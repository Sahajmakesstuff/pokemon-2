#importing modules
from pickle import TRUE
from Pokemon import *
import math
import random
from typechart import *

#trainer class
class Trainer:
    def __init__(self,name,pokemon_names):      #2 parameters name, list of pokemon
        self.name=name
        self.pokemon=[]
        self.opponent=0

        #making pokemon objects and adding to self.pokemon
        for i in pokemon_names:
            pokemon_i=Pokemon(i)
            self.pokemon.append(pokemon_i)

    #to print mons
    def print_mons(self):
        print("\nTrainer name is",self.name)
        for i in self.pokemon:
            i.nat_b()
            i.calc_stats()
            i.displaying()

    #function fight
    def fight(self,Player):

        #player is opponent
        self.opponent=Player

        #printing name and pokemon they sent about
        print("\nYou are fighting against",self.name)
        print("They sent out",self.pokemon[0].name)

        #calc stats
        self.pokemon[0].nat_b()
        self.pokemon[0].calc_stats()

        #pokemon we sent out
        print("\nYou sent out",self.opponent.pokemon[0].name)

        #var for while loop
        done=0
        while done==0:
            
            #printing current hp
            print("\nYour",self.opponent.pokemon[0].name,"is at",self.opponent.pokemon[0].hpIG,"HP")
            print("Opposing",self.pokemon[0].name,"is at",self.pokemon[0].hpIG,"HP")

            #printing our moves
            print("\nYour moves are:")
            for i in self.opponent.pokemon[0].moves:
                print(i.name)
            
            #taking input for move
            move_chosen=input("\nWhich Move would you like to Use? ")

            try:
                move_chosen=int(move_chosen)

                #if valid move
                if move_chosen>0 and move_chosen<5:
                    move_used=self.opponent.pokemon[0].moves[move_chosen-1].name

                    #var for stab
                    stab_p=1

                    #if same type
                    if self.opponent.pokemon[0].moves[move_chosen-1].type==self.opponent.pokemon[0].type:
                        stab_p=1.5
                    
                    #variables for crit
                    crit_dmg_p=1
                    crit_var_p=random.randrange(1,17)
                    critical_hit=False

                    #if 1/16 chance met, then crit
                    if crit_var_p==10:
                        critical_hit=True
                        crit_dmg_p=1.5
                    
                    #random variable
                    rand_p=random.randrange(8,11)
                    rand_p=rand_p/10

                    #effectiveness vars
                    effect_p=1
                    super_effective=False
                    not_effective=False

                    #if super effective
                    if self.opponent.pokemon[0].moves[move_chosen-1].type in type_chart[self.pokemon[0].type][1]:
                        effect_p=2
                        super_effective=True

                    #if not very effective
                    elif self.opponent.pokemon[0].moves[move_chosen-1].type in type_chart[self.pokemon[0].type][0]:
                        effect_p=0.5
                        not_effective=True

                    #damage calculations
                    damage_p=math.ceil((((22*self.opponent.pokemon[0].moves[move_chosen-1].power*
                                    self.opponent.pokemon[0].att/self.pokemon[0].defe)/25)+2)*
                                    stab_p *rand_p *effect_p *crit_dmg_p)

                    #if it does more than amount of hp
                    if damage_p>self.pokemon[0].hpIG:
                        damage_p=self.pokemon[0].hpIG

                    #calcing new hp
                    self.pokemon[0].hpIG=self.pokemon[0].hpIG-damage_p
                    
                    #stab for comp
                    stab_c=1

                    #effectiveness vars for comp
                    effectiveness_c=1
                    Super_c=False
                    Not_c=False

                    #list for move damages
                    move_dmgs_c=[]
                    
                    for i in range(0,4):
                        #shortening name
                        info_move_i=self.pokemon[0].moves[i]

                        #if same type
                        if info_move_i.type==self.pokemon[0].type:
                            stab_c=1.5
                        
                        #not same type
                        else:
                            stab_c=1
                        
                        #if super effective
                        if info_move_i.type in type_chart[self.opponent.pokemon[0].type][1]:
                            effectiveness_c=2 
                            Super_c=True

                        #not very effective
                        elif info_move_i.type in type_chart[self.opponent.pokemon[0].type][0]:
                            effectiveness_c=0.5
                            Not_c=True
                        
                        #neutral
                        else:
                            effectiveness_c=1
                            Super_c=False
                            Not_c=False
                        
                        #estimating damage
                        est_move_i=info_move_i.power*stab_c*effectiveness_c

                        #storing
                        move_i=[est_move_i,info_move_i.name,Super_c,Not_c]

                        #adding to list
                        move_dmgs_c.append(move_i)
                    
                    #sorting in descending order
                    move_dmgs_c.sort(reverse=True)

                    #2 choices
                    first_choice=move_dmgs_c[0]
                    second_choice=move_dmgs_c[1]

                    rand_for_choice=random.randrange(0,4)

                    #1st choice
                    if rand_for_choice!=3:
                        move_used=first_choice
                    
                    #2nd choice
                    else:
                        move_used=second_choice

                    #random var for comp
                    rand_c=random.randrange(8,11)
                    rand_c=rand_c/10

                    #crit vars for comp
                    crit_c=random.randrange(1,17)
                    crit_dmg_c=1
                    critical_c=False

                    #if crit
                    if crit_c == 6:
                        crit_dmg_c=1.5
                        critical_c=True
                    
                    #if not crit
                    else:
                        crit_dmg_c=1
                        critical_c=False
                    
                    #calcing comp damage
                    damage_c=math.ceil((((22*move_used[0]*
                                      self.pokemon[0].att/self.opponent.pokemon[0].defe)/25)+2)*
                                      rand_c*crit_dmg_c)

                    #capping maximum damage
                    if damage_c>self.opponent.pokemon[0].hpIG:
                        damage_c=self.opponent.pokemon[0].hpIG

                    #calcing new hp
                    self.opponent.pokemon[0].hpIG=self.opponent.pokemon[0].hpIG-damage_c

                    #if player is faster
                    if self.opponent.pokemon[0].spd>self.pokemon[0].spd:
                        #printing move used
                        print("\nYour",self.opponent.pokemon[0].name,"used",self.opponent.pokemon[0].moves[move_chosen-1].name)

                        #displaying text if super effective, not very effective, or crit
                        if super_effective==True:
                            print("The",self.opponent.pokemon[0].moves[move_chosen-1].name,"was super Effective")
                        if not_effective==True:
                            print("The",self.opponent.pokemon[0].moves[move_chosen-1].name,"was not very Effective")

                        if critical_hit==True:
                            print("The",self.opponent.pokemon[0].moves[move_chosen-1].name,"Was a Critical Hit")
                        
                        #printing amount of damage done
                        print("The",self.opponent.pokemon[0].moves[move_chosen-1].name,"did",damage_p,"HP of damage")

                        #if player wins
                        if self.pokemon[0].hpIG<=0:
                            done=1
                            break
                        
                        #printing opp move used
                        print("\nThe Opposing",self.pokemon[0].name,"Used",move_used[1])

                        #super effective
                        if move_used[2]==True:
                            print("The",move_used[1],"Was Super Effective!")
                        
                        #not effective
                        if move_used[3]==True:
                            print("The",move_used[1],"was Not very Effective")

                        #critical hit
                        if critical_c==True:
                            print("The",move_used[1],"was A Critical Hit!")
                        
                        #printing damage
                        print("The",move_used[1],"Did",damage_c,"HP of damage")

                        #if comp wins
                        if self.opponent.pokemon[0].hpIG<=0:
                            done=2
                            break
                        
                    #if comp speed is more than player speed
                    if self.pokemon[0].spd>self.opponent.pokemon[0].spd:

                        #printing opp move used
                        print("\nThe Opposing",self.pokemon[0].name,"Used",move_used[1])

                        #super effective
                        if move_used[2]==True:
                            print("The",move_used[1],"Was Super Effective!")

                        #not effective
                        if move_used[3]==True:
                            print("The",move_used[1],"was Not very Effective")

                        #critical hit
                        if critical_c==True:
                            print("The",move_used[1],"was A Critical Hit!")
                        
                        #printing damage
                        print("The",move_used[1],"Did",damage_c,"HP of damage")

                        #if comp wins
                        if self.opponent.pokemon[0].hpIG<=0:
                            done=2
                            break

                        #printing move used
                        print("\nYour",self.opponent.pokemon[0].name,"used",self.opponent.pokemon[0].moves[move_chosen-1].name)

                        #displaying text if super effective, not very effective, or crit
                        if super_effective==True:
                            print("The",self.opponent.pokemon[0].moves[move_chosen-1].name,"was super Effective")
                        if not_effective==True:
                            print("The",self.opponent.pokemon[0].moves[move_chosen-1].name,"was not very Effective")

                        if critical_hit==True:
                            print("The",self.opponent.pokemon[0].moves[move_chosen-1].name,"Was a Critical Hit")
                        
                        #printing amount of damage done
                        print("The",self.opponent.pokemon[0].moves[move_chosen-1].name,"did",damage_p,"HP of damage")

                        #if player wins
                        if self.pokemon[0].hpIG<=0:
                            done=1
                            break

                #Invalid move
                else:
                    print("Invalid Move")                
            
            #Invalid move
            except ValueError as ve:
                print("Invalid Move")
        
        #player wins
        if done==1:
            print("\nThe Opposing",self.pokemon[0].name,"Fainted!")
            print("You defeated",self.name,"!")
        
        elif done==2:
            print("\n",self.opponent.pokemon[0].name,"Fainted!")
            print("You Lost to",self.name,"!")
            print("You Blacked out!")

    def heal(self):
        self.pokemon[0].hpIG=self.pokemon[0].hp
        print("\nYour Pokemon were healed back to full HP!")


