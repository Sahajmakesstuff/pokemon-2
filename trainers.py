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
