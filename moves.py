import random

bullet_seed_pow=[30,45,45,60,60,60,75,75,90]
rollout_pow=[30,60,60,90,90,90,120,120,150]
tail_slap_pow=[25,50,50,75,75,75,100,100,125]

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
    "Bullet Seed": Move("Bullet Seed","grass",random.choice(bullet_seed_pow),"physical",random.randrange(80,96)),

    "Thunderbolt": Move("Thunderbolt","electric",90,"special",95),
    "Thunder Shock": Move("Thunder Shock","electric",40,"special",95),
    "Discharge": Move("Discharge","electric",80,"special",95),
    "Spark": Move("Spark","electric",65,"physical",95),
    "Thunder Fang": Move("Thunder Fang","electric",65,"physical",90),
    "Thunder": Move("Thunder","electric",110,"special",70),
    "Thunder Punch": Move("Thunder Punch","electric",75,"physical",95),
    "Wild Charge": Move("Wild Charge","electric",90,"physical",90),

    "Ice Beam": Move("Ice Beam","ice",90,"special",95),
    "Icy Wind": Move("Icy Wind","ice",55,"special",95),
    "Blizzard": Move("Blizzard","ice",110,"special",70),
    "Ice Shard": Move("Ice Shard","ice",40,"physical",95),
    "Icicle Crash": Move("Icicle Crash","ice",80,"physical",90),
    "Ice Fang": Move("Ice Fang","ice",65,"physical",90),
    "Ice Punch": Move("Ice Punch","ice",75,"physical",95),
    "Powder Snow": Move("Powder Snow","ice",40,"special",95),

    "Dragon Claw": Move("Dragon Claw","dragon",80,"physical",95),
    "Dragon Breath": Move("Dragon Breath","dragon",60,"special",95),
    "Draco Meteor": Move("Draco Meteor","dragon",130,"special",85),
    "Dragon Pulse": Move("Dragon Pulse","dragon",85,"special",95),
    "Outrage": Move("Outrage","dragon",120,"physical",90),
    "Twister": Move("Twister","dragon",40,"special",95),
    "Dragon Tail": Move("Dragon Tail","dragon",60,"physical",90),
    "Dual Chop": Move("Dual Chop","dragon",80,"physical",95),

    "Earthquake": Move("Earthquake","ground",100,"physical",95),
    "Sand Tomb": Move("Sand Tomb","ground",35,"special",85),
    "Dig": Move("Dig","ground",60,"physical",95),
    "Bulldoze": Move("Bulldoze","ground",60,"physical",95),
    "Mud Bomb": Move("Mud Bomb","ground",65,"special",80),
    "Stomping Tantrum": Move("Stomping Tantrum","ground",75,"physical",95),
    "Mud Slap": Move("Mud Slap","ground",20,"special",95),
    "High Horsepower": Move("High Horsepower","ground",95,"physical",90),

    "Rock Slide": Move("Rock Slide","rock",75,"physical",90),
    "Rock Tomb": Move("Rock Tomb","rock",60,"physical",85),
    "Stone Edge": Move("Stone Edge","rock",100,"physical",80),
    "Power Gem": Move("Power Gem","rock",80,"special",95),
    "Ancient Power": Move("Ancient Power","rock",60,"special",95),
    "Rollout": Move("Rollout","rock",random.choice(rollout_pow),"physical",random.randrange(75,91)),
    "Head Smash": Move("Head Smash","rock",150,"physical",80),
    "Rock Throw": Move("Rock Throw","rock",40,"special",90),

    "Flash Cannon": Move("Flash Cannon","steel",80,"special",95),
    "Metal Claw": Move("Metal Claw","steel",50,"physical",95),
    "Iron Head": Move("Iron Head","steel",80,"physical",95),
    "Smart Strike": Move("Smart Strike","steel",70,"physical",100),
    "Meteor Mash": Move("Meteor Mash","steel",100,"physical",85),
    "Mirror Shot": Move("Mirror Shot","steel",65,"special",95),
    "Bullet Punch": Move("Bullet Punch","steel",40,"physical",95),
    "Steel Wing": Move("Steel Wing","steel",70,"physical",95),

    "Body Slam": Move("Body Slam","normal",80,"physical",95),
    "Tackle": Move("Tackle","normal",40,"physical",95),
    "Headbutt": Move("Headbutt","normal",70,"physical",95),
    "Strength": Move("Hyper Fang","normal",80,"physical",95),
    "Hyper Voice": Move("Hyper Voice","normal",90,"special",95),
    "Hyper Beam": Move("Hyper Beam","normal",150,"special",75),
    "Explosion": Move("Explosion","normal",250,"physical",50),
    "Tail Slap": Move("Tail Slap","normal",random.choice(tail_slap_pow),"physical",random.randrange(85,96)),

    "Moonblast": Move("Moonblast","fairy",95,"special",95),
    "Fairy Wind": Move("Fairy Wind","fairy",45,"special",95),
    "Dazzling Gleam": Move("Dazzling Gleam","fairy",80,"special",95),
    "Play Rough": Move("Play Rough","fairy",90,"physical",90),
    "Spirit Break": Move("Spirit Break","fairy",75,"physical",95),
    "Misty Explosion": Move("Misty Explosion","fairy",100,"physical",80),
    "Disarming Voice": Move("Draining Kiss","fairy",40,"special",95),
    "Draining Kiss": Move("Draining Kiss","fairy",50,"physical",95),

    "Brick Break": Move("Brick Break","fighting",75,"physical",95),
    "Karate Chop": Move("Karate Chop","fighting",50,"physical",95),
    "Aura Sphere": Move("Aura Sphere","fighting",80,"special",100),
    "Close Combat": Move("Close Combat","fighting",120,"physical",90),
    "Cross Chop": Move("Cross Chop","fighting",100,"physical",80),
    "Focus Blast": Move("Focus Blast","fighting",120,"special",70),
    "Rock Smash": Move("Rock Smash","fighting",40,"physical",95),
    "Superpower": Move("Superpower","fighting",120,"physical",85),

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