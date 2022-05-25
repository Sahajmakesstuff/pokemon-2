class Move:
    def __init__(self,name,type,power):
        self.name=name
        self.type=type
        self.power=power

#comment
moves = {
    "Flamethrower": Move("Flamethrower", "fire", 90),
    "Ember": Move("Ember","fire",40),
    "Surf": Move("Surf","water",90),
    "Water Gun": Move("Water Gun","water",40),
    "Solar Beam": Move("Solar Beam","grass",90),
    "Vine Whip": Move("Vine Whip","grass",40),
    "Thunderbolt": Move("Thunderbolt","electric",90),
    "Thundershock": Move("Thundershock","electric",40),
    "Ice Beam": Move("Ice Beam","ice",90),
    "Icy Wind": Move("Icy Wind","ice",55),
    "Dragon Claw": Move("Dragon Claw","dragon",80),
    "Dragon Breath": Move("Dragon Breath","dragon",60),
    "Earthquake": Move("Earthquake","ground",100),
    "Sand Tomb": Move("Sand Tomb","ground",35),
    "Rock Slide": Move("Rock Slide","rock",75),
    "Rock Tomb": Move("Rock Tomb","rock",60),
    "Flash Cannon": Move("Flash Cannon","steel",80),
    "Metal Claw": Move("Metal Claw","steel",50),
    "Body Slam": Move("Body Slam","normal",80),
    "Tackle": Move("Tackle","normal",40),
    "Moonblast": Move("Moonblast","fairy",95),
    "Fairy Wind": Move("Fairy Wind","fairy",45),
    "Brick Break": Move("Brick Break","fighting",75),
    "Karate Chop": Move("Karate Chop","fighting",50)
}