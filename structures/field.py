import random
import numpy as np

from helpers.consts import MAX_AGENTS_COUNT, FOOD_COLOR_MAP
from helpers.helper import create2dimFieldOfCells, random2dPoints
from structures.cell import Cell


class Field:
    def __init__(self, N_dim, max_food, agents, part_foody_cells):
        self.N_dim = N_dim
        self.max_food_in_cell = max_food
        self.start_agents_count = agents
        self.part_of_cells_with_food = part_foody_cells

        self.polygon = create2dimFieldOfCells(N_dim)
        self.agents = self.start_agents_count
        self.max_agents = MAX_AGENTS_COUNT

    def create_food(self, quantity):
        """
            UPDATE FOOD IN THE WORLD
            count of food per tick == agents count
            update cells with new food data
            return 2d arr of cells , 2d arr of colored cells
        """
        new_cells_w_food = random2dPoints(self.N_dim, quantity)

        for i in range(quantity):
            x, y = new_cells_w_food[i]
            food_val = random.randint(1, self.max_food_in_cell)

            self.polygon[x][y] = Cell(x, y, food_val, FOOD_COLOR_MAP[food_val], self.max_food_in_cell)

        # transform polygon 2  arrs
        arr_of_cells_2d = self.polygon_2_arr()
        return arr_of_cells_2d, self.polygon_2_np_arr(arr_of_cells_2d)

    def check_cells_food_state(self):
        for row in self.polygon:
            for cell in row:
                if cell.food <= 0 and cell.color != 0:
                    print('[DEBUG] : Food in cell ended. color to 0')
                    cell.color = 0
                if cell.food > 0:
                    cell.color = FOOD_COLOR_MAP[cell.food]

    def polygon_2_arr(self):
        """
            Function returns 2d arrays of colored cells. Color gradient based on food val
        """
        polygon_arr = []
        for row in self.polygon:
            polygon_arr_row = []
            for cell in row:
                polygon_arr_row.append(FOOD_COLOR_MAP[cell.food])

            polygon_arr.append(polygon_arr_row)

        return polygon_arr

    def polygon_2_np_arr(self, field_2d_arr_colored):
        """
            For drawing plot . transform to np arr
        """
        return np.array(field_2d_arr_colored)
