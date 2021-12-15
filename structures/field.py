import random

from helpers.consts import MAX_AGENTS_COUNT
from helpers.helper import create2dimFieldOfCells, random2dPoints
from structures.cell import Cell


class Field:
    def __init__(self, N_dim, max_food, agents, part_foody_cells):
        self.N_dim = N_dim
        self.max_food_in_cell = max_food
        self.start_agents_count = agents
        self.part_of_cells_with_food = part_foody_cells

        self.polygon, self.polygon_arr = create2dimFieldOfCells(N_dim)
        self.agents = self.start_agents_count
        self.max_agents = MAX_AGENTS_COUNT

    def create_food(self, quantity):
        """
            CREATE FOOD IN THE WORLD
            count of food per tick == agents count
            update cells with new food data 
        """
        new_cells_w_food = random2dPoints(self.N_dim, quantity)

        for i in range(self.agents):
            x, y = new_cells_w_food[i]
            self.polygon[x][y] = Cell(x, y, random.randint(1, self.max_food_in_cell), '', self.max_food_in_cell)
