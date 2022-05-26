#The move class
class Move:
    def __init__(self,name,type,power,contact): #3 parameters name,type,power for each move
        self.name=name
        self.type=type
        self.power=power
        self.contact=contact

#move list
moves = {
    "Flamethrower": Move("Flamethrower", "fire", 90,"special"),
    "Ember": Move("Ember","fire",40,"special"),
    "Surf": Move("Surf","water",90,"special"),
    "Water Gun": Move("Water Gun","water",40,"special"),
    "Solar Beam": Move("Solar Beam","grass",90,"special"),
    "Vine Whip": Move("Vine Whip","grass",40,"physical"),
    "Thunderbolt": Move("Thunderbolt","electric",90,"special"),
    "Thundershock": Move("Thundershock","electric",40,"special"),
    "Ice Beam": Move("Ice Beam","ice",90,"special"),
    "Icy Wind": Move("Icy Wind","ice",55,"special"),
    "Dragon Claw": Move("Dragon Claw","dragon",80,"physical"),
    "Dragon Breath": Move("Dragon Breath","dragon",60,"special"),
    "Earthquake": Move("Earthquake","ground",100,"physical"),
    "Sand Tomb": Move("Sand Tomb","ground",35,"special"),
    "Rock Slide": Move("Rock Slide","rock",75,"physical"),
    "Rock Tomb": Move("Rock Tomb","rock",60,"physical"),
    "Flash Cannon": Move("Flash Cannon","steel",80,"special"),
    "Metal Claw": Move("Metal Claw","steel",50,"physical"),
    "Body Slam": Move("Body Slam","normal",80,"physical"),
    "Tackle": Move("Tackle","normal",40,"physical"),
    "Moonblast": Move("Moonblast","fairy",95,"special"),
    "Fairy Wind": Move("Fairy Wind","fairy",45,"special"),
    "Brick Break": Move("Brick Break","fighting",75,"physical"),
    "Karate Chop": Move("Karate Chop","fighting",50,"physical")
}