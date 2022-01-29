from utils.constants import characterATK, characterType


PLAYER_1 = {
    "CHARACTER": characterType.NONE,
    "HEALTH": 100,
    "POS": [0, 0],
}

PLAYER_2 = {
    "CHARACTER": characterType.NONE,
    "HEALTH": 100,
    "POS": [0, 0],
}


ATKS = {
    characterType.FIRE: {
        characterATK.ATK_1: 0,
        characterATK.ATK_2: 0,
        characterATK.ATK_3: 0,
        characterATK.ATK_SP: 0,
    },
    characterType.EARTH: {
        characterATK.ATK_1: 0,
        characterATK.ATK_2: 0,
        characterATK.ATK_3: 0,
        characterATK.ATK_SP: 0,
    },
    characterType.WATER: {
        characterATK.ATK_1: 0,
        characterATK.ATK_2: 0,
        characterATK.ATK_3: 0,
        characterATK.ATK_SP: 0,
    },
    characterType.AIR: {
        characterATK.ATK_1: 0,
        characterATK.ATK_2: 0,
        characterATK.ATK_3: 0,
        characterATK.ATK_SP: 0,
    },
}
