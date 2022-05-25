import random
import math
from moves import *

list_nat=["lonely","brave","gentle","relaxed","timid","hasty","bashful"]

class Pokemon:
    def __init__(self,name):
        self.name=name
        self.nature=random.choice(list_nat)
        self.moves=[]

        self.hp_IV=random.randrange(0,32)
        self.att_IV=random.randrange(0,32)
        self.def_IV=random.randrange(0,32)
        self.spd_IV=random.randrange(0,32)

        self.att_b=1
        self.def_b=1
        self.spd_b=1

        if self.name=="Flamey":
            self.type="fire"
            self.lvl=50
            self.base_hp=80
            self.base_att=100
            self.base_def=70
            self.base_spd=110

            self.moves=[
                moves["Flamethrower"],
                moves["Ember"],
                moves["Tackle"],
                moves["Earthquake"]
            ]
            
        elif self.name=="Bubbly":
            self.type="water"
            self.lvl=50
            self.base_hp=100
            self.base_att=90
            self.base_def=100
            self.base_spd=70

            self.moves=[
                moves["Surf"],
                moves["Water Gun"],
                moves["Tackle"],
                moves["Ice Beam"]
            ]
        
        elif self.name=="Leafy":
            self.type="grass"
            self.lvl=50
            self.base_hp=75
            self.base_att=105
            self.base_def=100
            self.base_spd=80

            self.moves=[
                moves["Solar Beam"],
                moves["Vine Whip"],
                moves["Tackle"],
                moves["Body Slam"]
            ]
        
        elif self.name=="Zapper":
            self.type="electric"
            self.lvl=50
            self.base_hp=75
            self.base_att=100
            self.base_def=60
            self.base_spd=125

            self.moves=[
                moves["Thunderbolt"],
                moves["Thundershock"],
                moves["Tackle"],
                moves["Flash Cannon"]
            ]
        
        elif self.name=="Icy":
            self.type="ice"
            self.lvl=50
            self.base_hp=60
            self.base_att=110
            self.base_def=80
            self.base_spd=110

            self.moves=[
                moves["Ice Beam"],
                moves["Icy Wind"],
                moves["Tackle"],
                moves["Moonblast"]
            ]
        
        elif self.name=="Dracomenace":
            self.type="dragon"
            self.lvl=50
            self.base_hp=100
            self.base_att=100
            self.base_def=80
            self.base_spd=80

            self.moves=[
                moves["Dragon Claw"],
                moves["Dragon Breath"],
                moves["Tackle"],
                moves["Earthquake"]
            ]
        
        elif self.name=="Groundian":
            self.type="ground"
            self.lvl=50
            self.base_hp=90
            self.base_att=125
            self.base_def=80
            self.base_spd=60

            self.moves=[
                moves["Earthquake"],
                moves["Sand Tomb"],
                moves["Tackle"],
                moves["Rock Slide"]
            ]

        elif self.name=="Stoney":
            self.type="rock"
            self.lvl=50
            self.base_hp=70
            self.base_att=105
            self.base_def=130
            self.base_spd=55

            self.moves=[
                moves["Rock Slide"],
                moves["Rock Tomb"],
                moves["Tackle"],
                moves["Earthquake"]
            ]
        
        elif self.name=="Metaleon":
            self.type="steel"
            self.lvl=50
            self.base_hp=130
            self.base_att=80
            self.base_def=100
            self.base_spd=50

            self.moves=[
                moves["Flash Cannon"],
                moves["Metal Claw"],
                moves["Tackle"],
                moves["Earthquake"]
            ]
        
        elif self.name=="Chunky":
            self.type="normal"
            self.lvl=50
            self.base_hp=140
            self.base_att=80
            self.base_def=100
            self.base_spd=40

            self.moves=[
                moves["Body Slam"],
                moves["Earthquake"],
                moves["Tackle"],
                moves["Flamethrower"]
            ]
        
        elif self.name=="Misteon":
            self.type="fairy"
            self.lvl=50
            self.base_hp=80
            self.base_att=95
            self.base_def=85
            self.base_spd=100

            self.moves=[
                moves["Moonblast"],
                moves["Fairy Wind"],
                moves["Tackle"],
                moves["Body Slam"]
            ]
        
        elif self.name=="Fisty":
            self.type="fighting"
            self.lvl=50
            self.base_hp=45
            self.base_att=130
            self.base_def=100
            self.base_spd=85

            self.moves=[
                moves["Brick Break"],
                moves["Karate Chop"],
                moves["Tackle"],
                moves["Earthquake"]
            ]

    def nat_b(self):
        if self.nature=="lonely":
            self.att_b=1.2
            self.def_b=0.8
            
        elif self.nature=="brave":
            self.att_b=1.2
            self.spd_b=0.8

        elif self.nature=="gentle":
            self.def_b=1.2
            self.att_b=0.8

        elif self.nature=="relaxed":
            self.def_b=1.2
            self.spd_b=0.8

        elif self.nature=="timid":
            self.spd_b=1.2
            self.att_b=0.8
            
        elif self.nature=="hasty":
            self.spd_b=1.2
            self.def_b=0.8

    def calc_stats(self):
        self.hp=math.ceil(self.base_hp*3+0.15*self.hp_IV)
        self.att=math.ceil((self.base_att*2+0.1*self.att_IV)*self.att_b)
        self.defe=math.ceil((self.base_def*2+0.1*self.def_IV)*self.def_b)
        self.spd=math.ceil((self.base_spd*2+0.1*self.spd_IV)*self.spd_b)
        self.stats=[self.hp,self.att,self.defe,self.spd]
    
    def displaying(self):
        print("\nName is:",self.name)
        print("Type is:",self.type)

        print("\nNature is:",self.nature)

        print("\nHP is",self.hp)
        print("Attack is",self.att)
        print("Defence is",self.defe)
        print("Speed is",self.spd)

        print("\nMoves are:")
        for i in self.moves:
            print(i.name)
