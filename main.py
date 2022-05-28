#importing from the other files
from Pokemon import *
from moves import *
from trainers import *

#printing flavour text
print("\nThere are 3 Pokemon for you to choose from")

#initializing flamey
fire_mon=Pokemon("Flamey")
fire_mon.nat_b()
fire_mon.calc_stats()
fire_mon.displaying()

#initializing bubbly
water_mon=Pokemon("Bubbly")
water_mon.nat_b()
water_mon.calc_stats()
water_mon.displaying()

#initializing leafy
grass_mon=Pokemon("Leafy")
grass_mon.nat_b()
grass_mon.calc_stats()
grass_mon.displaying()

#done choosing variable for while loop
d_choosing=0

#list for our pokemon
our_mons=[]

while d_choosing==0:
    #taking input for choosing
    chosen=input("\nWhich one would you like to choose? \n(Enter Number from 1-3 corresponding to the Pokemon) ")

    try:
        chosen_int=int(chosen)
        
        #if valid
        if chosen_int>0 and chosen_int<4:

            #flamey
            if chosen_int==1:
                print("\nYou Chose Flamey, The Fire Type Pokemon!")
                our_mons.append(fire_mon)
                d_choosing=1
            
            #bubbly
            elif chosen_int==2:
                print("\nYou Chose Bubbly, The Water Type Pokemon!")
                our_mons.append(water_mon)
                d_choosing=1

            #leafy
            else:
                print("\nYou Chose Leafy, The Grass Type Pokemon!")
                our_mons.append(grass_mon)
                d_choosing=1
        
        #invalid
        else:
            print("Invalid Pokemon")

    #Invalid
    except ValueError as ve:
        print("Invalid Pokemon")

#making player object and making his pokemon=our_mons
player=Trainer("player",[])
player.pokemon =  our_mons

#list of mons
available_mons=["Zapper","Icy","Dracomenace", "Groundian",
               "Stoney","Metaleon","Chunky","Misteon","Fisty",
               "Nasty","Brainy","Spooky",
               "Birdy","Beetlebug","Sludgemound"]

#list of names
trainer_names=["Bill","Abigail","Sam","Chris","Marissa",
              "James","Joey","Tristan","Timmy","Charlie"]

#no of battles
battles=input("\nEnter the Number of battles which you would like to have \n(Minimum is 3, Maximum is 10) ")

try:
    battles=int(battles)

    #if valid
    if battles>2 and battles<11:
        for i in range(0,battles):

            #choosing random mon
            trainer_i_mon=random.choice(available_mons)
            available_mons.remove(trainer_i_mon)
            trainer_i_mons=[]
            trainer_i_mons.append(trainer_i_mon)

            #choosing random name
            trainer_i_name=random.choice(trainer_names)
            trainer_names.remove(trainer_i_name)

            #making Trainer object
            trainer_i=Trainer(trainer_i_name,trainer_i_mons)

            #fighting with player
            trainer_i.fight(player)

            #healing player's pokemon's health
            player.heal()

            #press enter to start next battle
            if i !=battles-1:
                input("\nPress Enter to start next battle ")

    #Invalid
    else:
        print("Invalid Number")

#invalid
except ValueError as ve:
    print("Invalid Number")

#all battles have ended, no of wins and losses
print("\nAll The Battles have ended!")
print("\nYou got",player.wins,"Win(s) &",player.losses,"Loss(es)")

input("\nPress Enter to exit ")