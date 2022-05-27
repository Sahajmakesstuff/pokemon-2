import random

bullet_seed_pow=[30,45,45,60,60,60,75,75,90]
rollout_pow=[30,60,60,90,90,90,120,120,150]
tail_slap_pow=[25,50,50,75,75,75,100,100,125]

#Secondary effects
#Burn Recoil crit -def -acc flinch -spdef heal from opp -2 spatt user paralysis freeze priority
#confuse user -spd omniboost +user att recharge kill user

#The move class
class Move:
    def __init__(self,name,type,power,contact,accuracy,effect_chance,effect): 
        self.name=name
        self.type=type
        self.power=power
        self.contact=contact
        self.accuracy=accuracy
        self.effect_chance=effect_chance
        self.effect=effect

#move list
moves = {
    "Flamethrower": Move("Flamethrower", "fire", 90,"special",95,10,"Burn"),
    "Ember": Move("Ember","fire",40,"special",95,10,"Burn"),
    "Fire Blast": Move("Fire Blast","fire",110,"special",85,10,"Burn"),
    "Fire Punch": Move("Fire Punch","fire",75,"physical",95,10,"Burn"),
    "Flare Blitz": Move("Flare Blitz","fire",120,"physical",85,100,"Recoil"),
    "Fire Fang": Move("Fire Fang","fire",65,"physical",90,10,"Burn"),
    "Heat Wave": Move("Heat Wave","fire",95,"special",90,10,"Burn"),
    "Lava Plume": Move("Lava Plume","fire",80,"special",95,30,"Burn"),

    "Surf": Move("Surf","water",90,"special",95,0,"none"),
    "Water Gun": Move("Water Gun","water",40,"special",95,0,"none"),
    "Crabhammer": Move("Crabhammer","water",100,"physical",90,100,"crits"),
    "Hydro Pump": Move("Hydro Pump","water",110,"special",80,0,"none"),
    "Liquidation": Move("Liquidation","water",85,"physical",95,20,"-def"),
    "Muddy Water": Move("Muddy Water","water",90,"special",85,30,"-acc"),
    "Scald": Move("Scald","water",80,"special",95,30,"burn"),
    "Waterfall": Move("Waterfall","water",80,"physical",95,20,"flinch"),

    "Energy Ball": Move("Solar Beam","grass",90,"special",95,10,"-spdef"),
    "Vine Whip": Move("Vine Whip","grass",40,"physical",95,0,"none"),
    "Seed Bomb": Move("Seed Bomb","grass",80,"physical",95,0,"none"),
    "Mega Drain": Move("Mega Drain","grass",40,"special",95,100,"heal from opp"),
    "Giga Drain": Move("Giga Drain","grass",75,"special",95,100,"heal from opp"),
    "Leaf Blade": Move("Leaf Blade","grass",90,"physical",95,100,"crits"),
    "Leaf Storm": Move("Leaf Storm","grass",130,"special",80,100,"-2 spatt user"),
    "Bullet Seed": Move("Bullet Seed","grass",random.choice(bullet_seed_pow),"physical",random.randrange(80,96),0,"none"),

    "Thunderbolt": Move("Thunderbolt","electric",90,"special",95,10,"paralysis"),
    "Thunder Shock": Move("Thunder Shock","electric",40,"special",95,10,"paralysis"),
    "Discharge": Move("Discharge","electric",80,"special",95,30,"paralysis"),
    "Spark": Move("Spark","electric",65,"physical",95,30,"paralysis"),
    "Thunder Fang": Move("Thunder Fang","electric",65,"physical",90,10,"flinch"),
    "Thunder": Move("Thunder","electric",110,"special",70,30,"paralysis"),
    "Thunder Punch": Move("Thunder Punch","electric",75,"physical",95,10,"paralysis"),
    "Wild Charge": Move("Wild Charge","electric",90,"physical",90,100,"recoil"),

    "Ice Beam": Move("Ice Beam","ice",90,"special",95,30,"freeze"),
    "Icy Wind": Move("Icy Wind","ice",55,"special",95,30,"freeze"),
    "Blizzard": Move("Blizzard","ice",110,"special",70,30,"freeze"),
    "Ice Shard": Move("Ice Shard","ice",40,"physical",95,100,"priority"),
    "Icicle Crash": Move("Icicle Crash","ice",80,"physical",90,30,"flinch"),
    "Ice Fang": Move("Ice Fang","ice",65,"physical",90,10,"flinch"),
    "Ice Punch": Move("Ice Punch","ice",75,"physical",95,30,"freeze"),
    "Powder Snow": Move("Powder Snow","ice",40,"special",95,30,"freeze"),

    "Dragon Claw": Move("Dragon Claw","dragon",80,"physical",95,0,"none"),
    "Dragon Breath": Move("Dragon Breath","dragon",60,"special",95,30,"paralysis"),
    "Draco Meteor": Move("Draco Meteor","dragon",130,"special",85,100,"-2 spatt user"),
    "Dragon Pulse": Move("Dragon Pulse","dragon",85,"special",95,0,"none"),
    "Outrage": Move("Outrage","dragon",120,"physical",90,30,"confuse user"),
    "Twister": Move("Twister","dragon",40,"special",95,20,"flinch"),
    "Dragon Tail": Move("Dragon Tail","dragon",60,"physical",90,20,"flinch"),
    "Dual Chop": Move("Dual Chop","dragon",80,"physical",95,0,"none"),

    "Earthquake": Move("Earthquake","ground",100,"physical",95,0,"none"),
    "Sand Tomb": Move("Sand Tomb","ground",35,"special",85,10,"-acc"),
    "Dig": Move("Dig","ground",60,"physical",95,0,"none"),
    "Bulldoze": Move("Bulldoze","ground",60,"physical",95,10,"-spd"),
    "Mud Bomb": Move("Mud Bomb","ground",65,"special",80,30,"-acc"),
    "Stomping Tantrum": Move("Stomping Tantrum","ground",75,"physical",95,0,"none"),
    "Mud Slap": Move("Mud Slap","ground",20,"special",95,30,"-acc"),
    "High Horsepower": Move("High Horsepower","ground",95,"physical",90,0,"none"),

    "Rock Slide": Move("Rock Slide","rock",75,"physical",90,30,"flinch"),
    "Rock Tomb": Move("Rock Tomb","rock",60,"physical",85,30,"-spd"),
    "Stone Edge": Move("Stone Edge","rock",100,"physical",80,100,"crits"),
    "Power Gem": Move("Power Gem","rock",80,"special",95,10,"-spdef"),
    "Ancient Power": Move("Ancient Power","rock",60,"special",95,30,"omniboost"),
    "Rollout": Move("Rollout","rock",random.choice(rollout_pow),"physical",random.randrange(75,91),0,"none"),
    "Head Smash": Move("Head Smash","rock",150,"physical",80,100,"recoil"),
    "Rock Throw": Move("Rock Throw","rock",40,"special",90,0,"none"),

    "Flash Cannon": Move("Flash Cannon","steel",80,"special",95,10,"-spdef"),
    "Metal Claw": Move("Metal Claw","steel",50,"physical",95,10,"-def"),
    "Iron Head": Move("Iron Head","steel",80,"physical",95,30,"flinch"),
    "Smart Strike": Move("Smart Strike","steel",70,"physical",100,0,"none"),
    "Meteor Mash": Move("Meteor Mash","steel",100,"physical",85,20,"+ user att"),
    "Mirror Shot": Move("Mirror Shot","steel",65,"special",95,30,"-acc"),
    "Bullet Punch": Move("Bullet Punch","steel",40,"physical",95,100,"priority"),
    "Steel Wing": Move("Steel Wing","steel",70,"physical",95,10,"-def"),

    "Body Slam": Move("Body Slam","normal",80,"physical",95,30,"paralysis"),
    "Tackle": Move("Tackle","normal",40,"physical",95,0,"none"),
    "Headbutt": Move("Headbutt","normal",70,"physical",95,30,"flinch"),
    "Strength": Move("Hyper Fang","normal",80,"physical",95,0,"none"),
    "Hyper Voice": Move("Hyper Voice","normal",90,"special",95,0,"none"),
    "Hyper Beam": Move("Hyper Beam","normal",150,"special",75,100,"recharge"),
    "Explosion": Move("Explosion","normal",250,"physical",50,100,"kill user"),
    "Tail Slap": Move("Tail Slap","normal",random.choice(tail_slap_pow),"physical",random.randrange(85,96),30,"flinch"),

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
    "Crunch": Move("Crunch","dark",80,"physical",95),
    "Bite": Move("Bite","dark",60,"physical",95),
    "Night Slash": Move("Night Slash","dark",70,"physical",95),
    "Snarl": Move("Snarl","dark",50,"special",95),
    "Sucker Punch": Move("Sucker Punch","dark",70,"physical",95),
    "Throat Chop": Move("Throat Chop","dark",80,"physical",95),

    "Psychic": Move("Psychic","psychic",90,"special",95),
    "Psybeam": Move("Psybeam","psychic",65,"special",95),
    "Psyche Punch": Move("Psyche Punch","psychic",90,"physical",95),
    "Confusion": Move("Confusion","psychic",50,"special",95),
    "Psyshock": Move("Psyshock","psychic",80,"special",95),
    "Zen Headbutt": Move("Zen Headbutt","psychic",80,"psychic",90),
    "Psycho Cut": Move("Psycho Cut","psychic",70,"physical",95),
    "Psywave": Move("Psywave","psychic",25,"special",75),

    "Shadow Ball": Move("Shadow Ball","ghost",80,"special",95),
    "Shadow Claw": Move("Shadow Claw","ghost",65,"physical",90),
    "Hex": Move("Hex","ghost",65,"special",95),
    "Shadow Punch": Move("Shadow Punch","ghost",75,"physical",95),
    "Lick": Move("Lick","ghost",30,"physical",95),
    "Shadow Sneak": Move("Shadow Sneak","ghost",40,"physical",95),
    "Poltergeist": Move("Poltergeist","ghost",110,"physical",85),
    "Ominous Wind": Move("Ominous Wind","ghost",60,"special",95),

    "Brave Bird": Move("Brave Bird","flying",120,"physical",90),
    "Aerial Ace": Move("Aerial Ace","flying",60,"physical",100),
    "Gust": Move("Gust","flying",40,"special",95),
    "Air Slash": Move("Air Slash","flying",75,"special",95),
    "Fly": Move("Fly","flying",90,"physical",85),
    "Drill Peck": Move("Drill Peck","flying",80,"physical",95),
    "Hurricane": Move("Hurricane","flying",110,"special",70),
    "Dual Wingbeat": Move("Dual Wingbeat","flying",80,"physical",80),

    "X-Scissor": Move("X-Scissor","bug",80,"physical",95),
    "Infestation": Move("Infestation","bug",10,"special",80),
    "Bug Buzz": Move("Bug Buzz","bug",90,"special",95),
    "Leech Life": Move("Leech Life","bug",80,"physical",95),
    "Silver Wind": Move("Silver Wind","bug",60,"special",95),
    "Megahorn": Move("Megahorn","bug",120,"physical",85),
    "Pin Missile": Move("Pin Missile","bug",random.choice(tail_slap_pow),"physical",random.randrange(85,96)),
    "Lunge": Move("Lunge","bug",80,"special",95),
    
    "Sludge Bomb": Move("Sludge Bomb","poison",90,"special",95),
    "Poison Jab": Move("Poison Jab","poison",80,"physical",95),
    "Sludge Wave": Move("Sludge Wave","poison",95,"special",90),
    "Gunk Shot": Move("Gunk Shot","poison",120,"physical",80),
    "Cross Poison": Move("Cross Poison","poison",70,"physical",95),
    "Venoshock": Move("Venoshock","poison",65,"special",95),
    "Poison Fang": Move("Poison Fang","poison",65,"physical",90),
    "Acid": Move("Acid","poison",40,"special",95),
}