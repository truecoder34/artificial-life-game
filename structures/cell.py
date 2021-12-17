

class Cell:
    def __init__(self, x, y, food, color, max_food):
        self.x = x
        self.y = y
        self.food = food
        self.color = color
        self.max_food = max_food
    
    def decrementFood(self, val=1):
        """
            Decrement food level in Cell by value (default 1)
            if Agent stays in cell should be happened
        """
        self.food = self.food - val
        print("[DEBUG] CELL: x-{} y-{} : Food data updated - Decrement. New value = {}".format(self.x, self.y, self.food))
    
    def incrementFood(self, val=0):
        '''
            Increment Food value in Cell by specified value;
            if Food in cell not empty and SUM(old food, new food) > MAX - set MAX
        '''
        if val > 0:
            if self.food + val > self.max_food:
                self.food = self.max_food
            else:
                self.food = self.food + val
        print("[DEBUG] CELL: x-{} y-{} : Food data updated - Increment. New value = {}".format(self.x, self.y, self.food))

