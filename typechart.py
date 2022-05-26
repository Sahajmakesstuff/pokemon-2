#dictionary for type chart
type_chart={
    "fire": [
        ["grass","ice","steel","fairy"],
        ["water","dragon","ground","rock"]
    ],
    "water": [
        ["fire","ice","ground","rock"],
        ["grass","electric","dragon"]
    ],
    "grass": [
        ["water","electric","ground","rock"],
        ["fire","ice","dragon","steel"]
    ],
    "electric": [
        ["water","steel"],
        ["grass","dragon","ground"]
    ],
    "ice": [
        ["grass","dragon","ground"],
        ["fire","water","rock","steel","fighting"]
    ],
    "dragon": [
        ["fire","water","grass","electric"],
        ["ice","steel","fairy"]
    ],
    "ground": [
        ["fire","electric","rock","steel"],
        ["water","grass","ice"]
    ],
    "rock": [
        ["fire","ice","normal"],
        ["water","grass","ground","steel","fighting"]
    ],
    "steel": [
        ["ice","dragon","rock","normal","fairy","grass"],
        ["fire","grass","electric","ground","fighting"]
    ],
    "normal": [
        [],
        ["rock","steel","fighting"]
    ],
    "fairy": [
        ["dragon","fighting"],
        ["fire","steel"]
    ],
    "fighting": [
        ["ice","rock","steel","normal"],
        ["fairy"]
    ]
}