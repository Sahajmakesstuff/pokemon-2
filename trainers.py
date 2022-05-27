#importing modules
from Pokemon import *
import math
import random
from typechart import *
from sec_effects import *

#trainer class
class Trainer:
    def __init__(self,name,pokemon_names):      #2 parameters name, list of pokemon
        self.name=name
        self.pokemon=[]
        self.opponent=0
        self.wins=0
        self.losses=0

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
            self.opponent.pokemon[0].flinch=False
            self.pokemon[0].flinch=False

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
                    #shortening name
                    move_used_p=self.opponent.pokemon[0].moves[move_chosen-1].name

                    #var for missing
                    Miss_p=False

                    #var for accuracy check
                    rand_acc_p=random.randrange(1,101)*100

                    #if we hit
                    if rand_acc_p<=self.opponent.pokemon[0].moves[move_chosen-1].accuracy*self.opponent.pokemon[0].accuracy:
                        Miss_p=False
                    
                    #if we miss
                    else:
                        Miss_p=True      

                    #var for stab
                    stab_p=1

                    #if same type
                    if self.opponent.pokemon[0].moves[move_chosen-1].type==self.opponent.pokemon[0].type:
                        stab_p=1.5
                    
                    #variables for crit
                    crit_dmg_p=1
                    crit_var_p=random.randrange(1,17)
                    critical_hit=False

                    #if move has boosted crit chance
                    if self.opponent.pokemon[0].moves[move_chosen-1].effect=="crits":
                        crit_var_p=random.randrange(1,8)
                        if crit_var_p==5:
                            critical_hit=True
                            crit_dmg_p=1.5

                    else:
                        #if 1/16 chance met, then crit
                        if crit_var_p==10:
                            critical_hit=True
                            crit_dmg_p=1.5
                    
                    #random variable
                    rand_p=random.randrange(8,11)
                    rand_p=rand_p/10

                    #vars for effectiveness
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

                    #var for damage
                    damage_p=0

                    #damage if it is a physical move
                    if self.opponent.pokemon[0].moves[move_chosen-1].contact=="physical":
                        damage_p=math.ceil(((((((2*self.opponent.pokemon[0].lvl)/5)+2)*
                                        self.opponent.pokemon[0].moves[move_chosen-1].power*
                                        self.opponent.pokemon[0].att/self.pokemon[0].defe)/25)+2)*
                                        stab_p *rand_p *effect_p *crit_dmg_p)
                    
                    #damage if it is a special move
                    elif self.opponent.pokemon[0].moves[move_chosen-1].contact=="special":
                        damage_p=math.ceil(((((((2*self.opponent.pokemon[0].lvl)/5)+2)*
                                        self.opponent.pokemon[0].moves[move_chosen-1].power*
                                        self.opponent.pokemon[0].spatt/self.pokemon[0].spdef)/25)+2)*
                                        stab_p *rand_p *effect_p *crit_dmg_p)

                    #if it does more than amount of hp
                    if damage_p>self.pokemon[0].hpIG:
                        damage_p=self.pokemon[0].hpIG                  
                    
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
                        move_i=[est_move_i,info_move_i.name,Super_c,Not_c,info_move_i.contact,info_move_i.accuracy,info_move_i]

                        #adding to list
                        move_dmgs_c.append(move_i)
                    
                    #sorting in descending order
                    move_dmgs_c.sort(reverse=True)

                    #2 choices
                    first_choice=move_dmgs_c[0]
                    second_choice=move_dmgs_c[1]

                    #rand var for chosing which move to use
                    rand_for_choice=random.randrange(0,4)

                    #list for move used
                    move_used=[]

                    #1st choice
                    if rand_for_choice!=3:
                        move_used=first_choice
                    
                    #2nd choice
                    else:
                        move_used=second_choice

                    #var for computer missing
                    miss_c=False

                    #accuracy check var for comp
                    rand_acc_c=random.randrange(1,101)*100

                    #if comp hits
                    if rand_acc_c<=move_used[5]*self.pokemon[0].accuracy:
                        miss_c=False
                    
                    #if comp misses
                    else:
                        miss_c=True                        

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

                    #var for comp damage
                    damage_c=0

                    #if physical
                    if move_used[4]=="physical":
                        damage_c=math.ceil((((22*move_used[0]*
                                        self.pokemon[0].att/self.opponent.pokemon[0].defe)/25)+2)*
                                        rand_c*crit_dmg_c)
                    
                    #if special
                    elif move_used[4]=="special":
                        damage_c=math.ceil((((22*move_used[0]*
                                        self.pokemon[0].spatt/self.opponent.pokemon[0].spdef)/25)+2)*
                                        rand_c*crit_dmg_c)

                    #capping maximum damage
                    if damage_c>self.opponent.pokemon[0].hpIG:
                        damage_c=self.opponent.pokemon[0].hpIG

                    #if player is faster
                    if self.opponent.pokemon[0].spd>self.pokemon[0].spd:
                        #if we don't miss
                        if Miss_p==False:

                            #calcing new hp
                            self.pokemon[0].hpIG=self.pokemon[0].hpIG-damage_p
                                
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

                            sec_eff(self.opponent.pokemon[0].moves[move_chosen-1],self.opponent.pokemon[0],self.pokemon[0],damage_p)

                            #if player wins
                            if self.pokemon[0].hpIG<=0:
                                done=1
                                break
                        
                        #if we miss
                        else:
                            print("\nThe",move_used_p,"Missed!")

                        #if computer hits
                        if miss_c==False:   
                            
                            #if pokemon didn't flinch
                            if self.pokemon[0].flinch==False:
                                #calcing new hp
                                self.opponent.pokemon[0].hpIG=self.opponent.pokemon[0].hpIG-damage_c

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

                                sec_eff(move_used[6],self.pokemon[0],self.opponent.pokemon[0],damage_c)

                                #if comp wins
                                if self.opponent.pokemon[0].hpIG<=0:
                                    done=2
                                    break
                            
                            #if flinched
                            else:
                                print("\nOpponent",self.pokemon[0].name,"Flinched and Couldn't Move")
                        
                        #if comp misses
                        else:
                            print("\nThe",move_used[1],"missed")

                        #if comp hurts from burn
                        if self.pokemon[0].status=="Burn" and self.pokemon[0].hpIG!=0:
                            self.pokemon[0].hpIG=math.ceil(self.pokemon[0].hpIG-(self.pokemon[0].hp*1/12))

                            #displaying text
                            print(self.pokemon[0].name,"Hurt from the Burn")

                            #capping burn damage
                            if self.pokemon[0].hpIG>0:
                                self.pokemon[0].hpIG=0
                                done=1

                    #if comp speed is more than player speed
                    elif self.opponent.pokemon[0].spd<self.pokemon[0].spd:

                        #if comp doesn't miss
                        if miss_c==False:

                            #calcing new hp
                            self.opponent.pokemon[0].hpIG=self.opponent.pokemon[0].hpIG-damage_c

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

                            sec_eff(move_used[6],self.pokemon[0],self.opponent.pokemon[0],damage_c)

                            #if comp wins
                            if self.opponent.pokemon[0].hpIG<=0:
                                done=2
                                break
                        
                        #if comp misses
                        else:
                            print("\nThe",move_used[1],"missed")

                        #if we don't miss
                        if Miss_p==False:

                            #if pokemon didn't flinch
                            if self.opponent.pokemon[0].flinch==False:
                                #calcing new hp
                                self.pokemon[0].hpIG=self.pokemon[0].hpIG-damage_p

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

                                sec_eff(self.opponent.pokemon[0].moves[move_chosen-1],self.opponent.pokemon[0],self.pokemon[0],damage_p)

                                #if player wins
                                if self.pokemon[0].hpIG<=0:
                                    done=1
                                    break
                            
                            #if flinched
                            else:
                                print("\nYour",self.opponent.pokemon[0].name,"Flinched and Couldn't Move")
                        
                        #if we miss
                        else:
                            print("\nThe",move_used_p,"Missed!")
                        
                        #if comp is hurt by burn
                        if self.pokemon[0].status=="Burn" and self.pokemon[0].hpIG!=0:
                            self.pokemon[0].hpIG=math.ceil(self.pokemon[0].hpIG-(self.pokemon[0].hp*1/12))
                            print(self.pokemon[0].name,"Hurt from the Burn")

                #Invalid move
                else:
                    print("Invalid Move")                
            
            #Invalid move
            except ValueError as ve:
                print("Invalid Move")
        
        #player wins
        if done==1:

            #opposing mon fainted and you defeated the person
            print("\nThe Opposing",self.pokemon[0].name,"Fainted!")
            print("You defeated",self.name,"!")

            #adding to wins and raising lvl of pokemon and displaying it
            self.opponent.wins+=1
            self.opponent.pokemon[0].lvl+=1
            print("\nYour",self.opponent.pokemon[0].name,"grew to Level",self.opponent.pokemon[0].lvl)

            #calculating new stats
            self.opponent.pokemon[0].newhp=math.ceil((self.opponent.pokemon[0].base_hp*3+0.15*self.opponent.pokemon[0].hp_IV*self.opponent.pokemon[0].lvl/50)+1)
            self.opponent.pokemon[0].att=math.ceil((self.opponent.pokemon[0].base_att*2+0.1*self.opponent.pokemon[0].att_IV)*self.opponent.pokemon[0].att_b*self.opponent.pokemon[0].lvl/50)
            self.opponent.pokemon[0].defe=math.ceil((self.opponent.pokemon[0].base_def*2+0.1*self.opponent.pokemon[0].def_IV)*self.opponent.pokemon[0].def_b*self.opponent.pokemon[0].lvl/50)
            self.opponent.pokemon[0].spd=math.ceil((self.opponent.pokemon[0].base_spd*2+0.1*self.opponent.pokemon[0].spd_IV)*self.opponent.pokemon[0].spd_b*self.opponent.pokemon[0].lvl/50)
            self.opponent.pokemon[0].spatt=math.ceil((self.opponent.pokemon[0].base_spatt*2+0.1*self.opponent.pokemon[0].spatt_IV)*self.opponent.pokemon[0].spatt_b*self.opponent.pokemon[0].lvl/50)
            self.opponent.pokemon[0].spdef=math.ceil((self.opponent.pokemon[0].base_spdef*2+0.1*self.opponent.pokemon[0].spdef_IV)*self.opponent.pokemon[0].spdef_b*self.opponent.pokemon[0].lvl/50)

            #difference in hp
            self.opponent.pokemon[0].hpdif=self.opponent.pokemon[0].newhp-self.opponent.pokemon[0].hp

            #minimum difference in hp
            if self.opponent.pokemon[0].hpdif==0:
                self.opponent.pokemon[0].hpdif=2

            #new hp
            self.opponent.pokemon[0].hp=self.opponent.pokemon[0].hp+self.opponent.pokemon[0].hpdif

            #Displaying new stats
            print("\nYour HP grew to",self.opponent.pokemon[0].hp)
            print("Your Attack grew to",self.opponent.pokemon[0].att)
            print("Your Defense grew to",self.opponent.pokemon[0].defe)    
            print("Your Speed grew to",self.opponent.pokemon[0].spd)       
            print("Your Special Attack grew to",self.opponent.pokemon[0].spatt) 
            print("Your Special Defense grew to",self.opponent.pokemon[0].spdef)
        
        #if player lost
        elif done==2:

            #your pokemon fainted and adding to losses
            print("\n",self.opponent.pokemon[0].name,"Fainted!")
            print("You Lost to",self.name,"!")
            print("You Blacked out!")
            self.opponent.losses+=1

    #heal function for player
    def heal(self):
        self.pokemon[0].hpIG=self.pokemon[0].hp
        print("\nYour Pokemon were healed back to full HP!")


