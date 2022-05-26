#importing from the other files
from Pokemon import *
from moves import *
from trainers import *

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

#list of mons
available_mons=["Flamey","Bubbly","Leafy","Zapper","Icy","Dracomenace",
                "Groundian","Stoney","Metaleon","Chunky","Misteon","Fisty"]

#making new trainer_1 Bill
trainer_1_mon=random.choice(available_mons)
trainer_1_mons=[]
trainer_1_mons.append(trainer_1_mon)
trainer_1=Trainer("Bill",trainer_1_mons)

#making player object and making his pokemon=our_mons
player=Trainer("player",[])
player.pokemon =  our_mons

#to make trainer_1 fight
trainer_1.fight(player)

player.heal()