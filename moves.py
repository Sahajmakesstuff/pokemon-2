#The move class
class Move:
    def __init__(self,name,type,power,contact,accuracy): #3 parameters name,type,power for each move
        self.name=name
        self.type=type
        self.power=power
        self.contact=contact
        self.accuracy=accuracy

#move list
moves = {
    "Flamethrower": Move("Flamethrower", "fire", 90,"special",95),
    "Ember": Move("Ember","fire",40,"special",95),
    "Fire Blast": Move("Fire Blast","fire",110,"special",85),
    "Fire Punch": Move("Fire Punch","fire",75,"physical",95),
    "Flare Blitz": Move("Flare Blitz","fire",120,"physical",85),
    "Fire Fang": Move("Fire Fang","fire",65,"physical",90),
    "Heat Wave": Move("Heat Wave","fire",95,"special",90),
    "Lava Plume": Move("Lava Plume","fire",80,"special",95),

    "Surf": Move("Surf","water",90,"special",95),
    "Water Gun": Move("Water Gun","water",40,"special",95),
    "Crabhammer": Move("Crabhammer","water",100,"physical",90),
    "Hydro Pump": Move("Hydro Pump","water",110,"special",80),
    "Liquidation": Move("Liquidation","water",85,"physical",95),
    "Muddy Water": Move("Muddy Water","water",90,"special",85),
    "Scald": Move("Scald","water",80,"special",95),
    "Waterfall": Move("Waterfall","water",80,"physical",95),

    "Energy Ball": Move("Solar Beam","grass",90,"special",95),
    "Vine Whip": Move("Vine Whip","grass",40,"physical",95),
    "Seed Bomb": Move("Seed Bomb","grass",80,"physical",95),
    "Mega Drain": Move("Mega Drain","grass",40,"special",95),
    "Giga Drain": Move("Giga Drain","grass",75,"special",95),
    "Leaf Blade": Move("Leaf Blade","grass",90,"physical",95),
    "Leaf Storm": Move("Leaf Storm","grass",130,"special",80),
    "Horn Leech": Move("Horn Leech","grass",75,"physical",95),

    "Thunderbolt": Move("Thunderbolt","electric",90,"special",95),
    "Thundershock": Move("Thundershock","electric",40,"special",95),

    "Ice Beam": Move("Ice Beam","ice",90,"special",95),
    "Icy Wind": Move("Icy Wind","ice",55,"special",95),

    "Dragon Claw": Move("Dragon Claw","dragon",80,"physical",95),
    "Dragon Breath": Move("Dragon Breath","dragon",60,"special",95),

    "Earthquake": Move("Earthquake","ground",100,"physical",95),
    "Sand Tomb": Move("Sand Tomb","ground",35,"special",85),

    "Rock Slide": Move("Rock Slide","rock",75,"physical",90),
    "Rock Tomb": Move("Rock Tomb","rock",60,"physical",85),

    "Flash Cannon": Move("Flash Cannon","steel",80,"special",95),
    "Metal Claw": Move("Metal Claw","steel",50,"physical",95),

    "Body Slam": Move("Body Slam","normal",80,"physical",95),
    "Tackle": Move("Tackle","normal",40,"physical",95),

    "Moonblast": Move("Moonblast","fairy",95,"special",95),
    "Fairy Wind": Move("Fairy Wind","fairy",45,"special",95),

    "Brick Break": Move("Brick Break","fighting",75,"physical",95),
    "Karate Chop": Move("Karate Chop","fighting",50,"physical",95),

    "Dark Pulse": Move("Dark Pulse","dark",80,"special",95),
    "Knock Off": Move("Knock Off","dark",65,"physical",95),

    "Psychic": Move("Psychic","psychic",90,"special",95),
    "Psybeam": Move("Psybeam","psychic",65,"special",95),

    "Shadow Ball": Move("Shadow Ball","ghost",80,"special",95),
    "Shadow Claw": Move("Shadow Claw","ghost",75,"physical",95),

    "Brave Bird": Move("Brave Bird","flying",120,"physical",90),
    "Aerial Ace": Move("Aerial Ace","flying",60,"physical",100),

    "X-Scissor": Move("X-Scissor","bug",80,"physical",95),
    "Infestation": Move("Infestation","bug",10,"special",80),
    
    "Sludge Bomb": Move("Sludge Bomb","poison",90,"special",95),
    "Poison Jab": Move("Poison Jab","poison",80,"physical",95)
}