# CELLS
N = 25                      # default
MAX_FOOD_IN_CELL = 5       # generates it randomly 1..15

FOOD_COLOR_MAP = {
    0: 0,
    1: 51,
    2: 102,
    3: 153,
    4: 204,
    5: 255
}

INITIAL_AGENTS_COUNT = 1
PART_OF_CELLS_WITH_FOOD = 0.1 * N * N   #  only 0.4 of total cells are with food

# ACTORS 
INITIAL_AGENTS_COUNT = 1
MAX_MENTAL_HEALTH = 15
MAX_PHISICAL_HEALTH = 30

SPLIT_COEFFICIENT_PHISICAL = 0.8

DECREMENT_PHISICAL_HEALTH = 0.8 * MAX_PHISICAL_HEALTH   # when split
DECREMENT_MENTAL_HEALTH = 1     # when move

UPDATE_INTERVAL = 1000

MAX_AGENTS_COUNT = 8

MAX_DEAD_TICKS = 3          # Agent with 0 mental health will die after 3 ticks

