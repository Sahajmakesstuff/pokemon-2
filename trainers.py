from Pokemon import *
class Trainer:
    def __init__(self,name,pokemon_names):
        self.name=name
        self.pokemon=[]

        for i in pokemon_names:
            pokemon_i=Pokemon(i)
            self.pokemon.append(pokemon_i)

    def print_mons(self):
        print("\nTrainer name is",self.name)
        for i in self.pokemon:
            i.nat_b()
            i.calc_stats()
            i.displaying()

def choose():
    print("\nThere are 3 Pokemon for you to choose from")

    fire_mon=Pokemon("Flamey")
    fire_mon.nat_b()
    fire_mon.calc_stats()
    fire_mon.displaying()

    water_mon=Pokemon("Bubbly")
    water_mon.nat_b()
    water_mon.calc_stats()
    water_mon.displaying()

    grass_mon=Pokemon("Leafy")
    grass_mon.nat_b()
    grass_mon.calc_stats()
    grass_mon.displaying()

    d_choosing=0

    while d_choosing==0:
        chosen=input("\nWhich one would you like to choose? \n(Enter Number from 1-3 corresponding to the Pokemon) ")

        try:
            chosen_int=int(chosen)
            our_mons=[]

            Player=Trainer("player",our_mons)

            if chosen_int>0 and chosen_int<4:
                if chosen_int==1:
                    print("\nYou Chose Flamey, The Fire Type Pokemon!")
                    our_mons.append(fire_mon)
                    d_choosing=1
                
                elif chosen_int==2:
                    print("\nYou Chose Bubbly, The Water Type Pokemon!")
                    our_mons.append(water_mon)
                    d_choosing=1

                else:
                    print("\nYou Chose Leafy, The Grass Type Pokemon!")
                    our_mons.append(grass_mon)
                    d_choosing=1
            
            else:
                print("Invalid Pokemon")

        except ValueError as ve:
            print("Invalid Pokemon")