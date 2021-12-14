import random
import uuid


class Agent:
    def __init__(self, name, n_dim, phisical, mental, split_coef_phisical, max_phisical_health, max_mental_health):
        self.name = name
        self.phisical_health = phisical
        self.mental_health = mental
        self.n_dim = n_dim
        self.x = random.randint(0, self.n_dim - 1)
        self.y = random.randint(0, self.n_dim - 1)

        self.state = True       # Means that MENTAL_HEALTH > 0

        self.split_coef_phisical = split_coef_phisical
        self.max_phisical_health = max_phisical_health
        self.max_mental_health = max_mental_health

        self.action_to_do = {}

    def split(self):
        '''
            Split this agent . Means create a new one with DEFAULT PARAMETERS
        '''
        new_agent = Agent(uuid.uuid4(), self.n_dim, self.max_phisical_health, self.max_mental_health,
                          self.split_coef_phisical, self.max_phisical_health, self.max_mental_health)
        self.phisical_health = self.phisical_health - self.split_coef_phisical * self.max_phisical_health  # remove data drom current after split
        print('[DEBUG] : New agent created! Name - {}, position X:{} - Y:{}'.format(new_agent.name, new_agent.x,
                                                                                    new_agent.y))
        return new_agent

    def eat(self, val=1):
        ''' eat food one per tick or more if specified'''
        # check that total phisical heatlh <= 30
        if self.phisical_health < self.max_phisical_health:
            self.phisical_health = self.phisical_health + val
            print('[DEBUG]: Agent {} eats. New PHISICAL HEALTH = {}'.format(self.name, self.phisical_health))
            return True
        else:
            print('[DEBUG]: Agent {} has MAXIMAL PHISICAL HEALTH. Don\'t eat.'.format(self.name))
            return False

    def choose_direction(self, field):
        '''
            Based on field choose the path
            go to first cell with food - else choose randomly
        '''
        new_x = 0
        new_y = 0
        # check border cases
        if (self.x + 1 >= self.n_dim) or (self.y + 1 >= self.n_dim) or (self.x - 1 < 0) or (self.y - 1 < 0):
            if self.x + 1 >= self.n_dim:
                new_x = 0
            if self.y + 1 >= self.n_dim:
                new_y = 0
            if self.x - 1 < 0:
                new_x = self.n_dim - 1
            if self.y - 1 < 0:
                new_y = self.n_dim - 1
        else:
            # male move when it is not a border case
            if field[self.x + 1][self.y].food > 0:
                new_x = self.x + 1
                new_y = self.y
            elif field[self.x - 1][self.y].food > 0:
                new_x = self.x - 1
                new_y = self.y
            elif field[self.x][self.y + 1].food > 0:
                new_x = self.x
                new_y = self.y + 1
            elif field[self.x][self.y - 1].food > 0:
                new_x = self.x
                new_y = self.y - 1
            else:
                # randomly choose one of 4 points
                neighbours = [[self.x + 1, self.y],
                              [self.x - 1, self.y],
                              [self.x, self.y + 1],
                              [self.x, self.y - 1]]
                rndm_idx = random.randint(0, 3)
                new_x, new_y = neighbours[rndm_idx]
        return new_x, new_y

    def move(self, polygon):
        '''
            Move agent to new coordinates and decrement MENTAL HEALTH
        '''
        if not self.die():
            self.x, self.y = self.choose_direction(polygon)
            print('[DEBUG] Agent {} coordinates are updated, new one: X:{} - Y:{}'.format(self.name, self.x, self.y))
            self.mental_health -= 1
            print('[DEBUG] Agent {} MENTAL HEALTH decremented, new MENTAL HEALTH = {}'.format(self.name, self.mental_health))
            if self.mental_health == 1:
                print('[DEBUG] ATTENTION ! Agent {} has 1 MENTAL HEALTH left'.format(self.name))
        else:
            print('[DEBUG] ATTENTION ! Agent {} has 0 MENTAL HEALTH left. He is almost dead...'.format(self.name))



    def die(self):
        # die only when phisical health <= 0 and this state is active > then 5 ticks
        if self.mental_health <= 0:
            self.state = False
            print('[DEBUG] ATTENTION ! Agent {} has 0 MENTAL HEALTH. Agent dying. It only can make split.'.format(
                self.name))
            # self.__del__()
            return True
        return False

    def act(self, field):
        '''
            Choose what to do by actor
            param 1 - field
            return - field with updated resources state,
                    updated agent's state,
                    new agent if it was created
        '''
        result = {
            "field": None,
            "agent": None,
            "new_agent": None
        }
        print('[DEBUG] Agent {} in cell X:{} - Y:{} is acting...'.format(self.name, self.x, self.y))

        if self.phisical_health > self.split_coef_phisical * self.max_phisical_health:
            print('[DEBUG] Agent {} in cell X:{} - Y:{} do SPLIT'.format(self.name, self.x, self.y))
            result['new_agent'] = self.split()
            result['agent'] = self
        #     pass
        elif field.polygon[self.x][self.y].food > 0:
            # 2 - EAT
            print('[DEBUG] FOOD IN CELL {}'.format(field.polygon[self.x][self.y].food))
            if not self.eat():
                # 2.1 - if full - move
                print('[DEBUG] Agent {} in cell X:{} - Y:{} do MOVE'.format(self.name, self.x, self.y))
                self.move(field.polygon)
                result['agent'] = self
            else:
                # 2.2 else - eat
                field.polygon[self.x][self.y].decrementFood()
                result['field'] = field
                result['agent'] = self
        else:
            print('[DEBUG] Agent {} in cell X:{} - Y:{} do MOVE'.format(self.name, self.x, self.y))
            self.move(field.polygon)
            result['agent'] = self

        # else:
        #     self.split()

        return result

    def __del__(self):
        print('[DEBUG] Agent {} is dead.'.format(self.name))
