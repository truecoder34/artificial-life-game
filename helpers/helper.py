import random
from helpers.consts import PART_OF_CELLS_WITH_FOOD, MAX_FOOD_IN_CELL, FOOD_COLOR_MAP
import numpy as np
from structures.cell import Cell


def random2dPoints(size, quantity=PART_OF_CELLS_WITH_FOOD):
    """
        param 1 : size of x and y dimensions
        return :  array of points with food;
    """
    result = []  # list of lists [ [x1,y1].., [xn,yn]]
    i = 0

    while i < quantity:
        random_x = random.randint(0, size - 1)
        random_y = random.randint(0, size - 1)

        if [random_x, random_y] not in result:
            result.append([random_x, random_y])
            i = i + 1

    return result


def create2dimFieldOfCells(size):
    """
        param 1 : size of x and y dimensions
        return :  2 dim array of CELLS;
    """
    polygon = []
    cells_with_food = random2dPoints(size)

    for i in range(size):
        polygon_row = []
        for j in range(size):
            if [i, j] in cells_with_food:
                food_to_cell = random.randint(1, MAX_FOOD_IN_CELL)
                cell = Cell(i, j, food_to_cell, FOOD_COLOR_MAP[food_to_cell], MAX_FOOD_IN_CELL)
            else:
                cell = Cell(i, j, 0, 0, MAX_FOOD_IN_CELL)

            polygon_row.append(cell)

        polygon.append(polygon_row)

    return polygon


def polygon_of_cells_2_colors_2d(field):
    """
        2-D Cells array (field) --to->  2-D Colors array
    """
    result = []
    for row in field:
        result_row = []
        for cell in row:
            result_row.append(cell.color)
        result.append(result_row)
    return result
