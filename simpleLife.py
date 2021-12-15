"""

Simple implementation of Game of Life. 

Author : Vladislav Plotnikov

"""

import sys, argparse
import uuid
from operator import attrgetter

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from conwayGameOfLife import randomGrid
from helpers.consts import *
from helpers.helper import create2dimFieldOfCells
from structures.agent import Agent
from structures.field import Field


class Simulation:
    def __init__(self,
                 n=N,
                 max_food=MAX_FOOD_IN_CELL,
                 agents=INITIAL_AGENTS_COUNT,
                 part_foody_cells=PART_OF_CELLS_WITH_FOOD,
                 update_interval=UPDATE_INTERVAL,
                 ) -> None:
        self.n_dim = n
        self.max_food = max_food
        self.agents_in_game = agents
        self.foody_cells = part_foody_cells
        self.upd_interval = update_interval

        self.agents_alive = set()

    def clean(self, ax):
        '''
            remove all agents from field
            param 1 - ax object (return by plt.subplot())
        '''
        # loop over all lines on the axis "ax" to remove
        for line in ax.lines:
            line.set_marker(None)

    def drawAgents(self, alive_agents, ax):
        '''
            draw all agents
            param 1 - list of alive agents (cells)
            param 2 - ax object (return by plt.subplot())
            return - nothing
        '''
        for agent in alive_agents:
            x, y = agent.x, agent.y
            ax.plot(x, y, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")

    # TODO : implement field update. How to renew food?
    '''
        params : state of game as input 
        
    '''
    def update(self, frameNum, img, grid_np, grid, field, ax):
        # copy grid since we require 8 neighbors for calculation
        # and we go line by line


        # redraw previous state before new move !

        print("[STATE-BEFORE]Currently alive agents {} . Total quantity = {}".format(self.agents_alive,
                                                                                     len(self.agents_alive)))
        print("[STATE-BEFORE]Currently alive agents {} . ".format(list(map(lambda x: x.name, self.agents_alive))))

        self.clean(ax)
        self.drawAgents(self.agents_alive, ax)



        print('[DEBUG] Quantity of acting ACTORS = {}'.format(len(self.agents_alive)))
        print('[DEBUG-STATE] {}/{} . {} - max allowed agents quantity '.format(len(self.agents_alive), field.max_agents,
                                                                               field.max_agents))

        new_agents = set()
        updated_agents = set()
        # each alive agent will act ordered by age
        for agent in self.agents_alive:
            result = agent.act(field)
            # process results before next step
            for key, value in result.items():
                if key == "field" and value is not None:
                    updated_agents.add(result['agent'])
                elif key == "agent" and value is not None:
                    # update fields of existing agent by new values
                    updated_agents.add(result['agent'])

                elif key == "new_agent" and value is not None:
                    new_agents.add(result['new_agent'])

        if len(new_agents) > 0 or len(updated_agents) > 0:
            print('[STATE-MIDDLE] Before overriding list of agents : {} . Total quantity = {}'.format(self.agents_alive,
                                                                                                     len(self.agents_alive)))
            print("[STATE-MIDDLE]Currently alive agents {} . ".format(list(map(lambda x: x.name, self.agents_alive))))
            self.agents_alive = updated_agents.union(new_agents)

            field.agents = len(self.agents_alive)

        print("[STATE-AFTER]Currently alive agents {} . Total quantity = {}".format(self.agents_alive,
                                                                                    len(self.agents_alive)))
        print("[STATE-AFTER]Currently alive agents {} . ".format(list(map(lambda x: x.name, self.agents_alive))))


        newGrid = grid.copy()
        newGrid_np = grid_np.copy()

        # field update - each turn - random update
        # polygon, polygon_arr = create2dimFieldOfCells(self.n_dim)
        # polygon_arr_np = np.array(polygon_arr)


        img.set_data(newGrid_np)
        grid[:] = newGrid_np[:]
        return img, 1

    def run(self):
        """
        1 - init field with food
        2 - create 1 agent . add it ti list of alive agent
        3 - start sim:
            _1 - agent check for food, eat once or move towards to food or randomly
        """
        field = Field(self.n_dim, self.max_food, self.agents_in_game, self.foody_cells)
        polygon, polygon_arr = field.polygon, field.polygon_arr
        agent = Agent(uuid.uuid4(), self.n_dim, MAX_PHISICAL_HEALTH, MAX_MENTAL_HEALTH, SPLIT_COEFFICIENT_PHISICAL,
                      MAX_PHISICAL_HEALTH, MAX_MENTAL_HEALTH)

        self.agents_alive.add(agent)

        polygon_arr_np = np.array(polygon_arr)  # move polygon to NP array.
        fig, ax = plt.subplots()  # draw initial field
        img = ax.imshow(polygon_arr_np, interpolation='nearest')

        ani = animation.FuncAnimation(fig, self.update,
                                      fargs=(img, polygon_arr_np, polygon_arr, field, ax),
                                      frames=10,
                                      interval=self.upd_interval,
                                      save_count=50)                 # set up animation

        # # of frames?
        # set output file




        plt.show()


def main():
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Artificial Conway's Game of Life simulation.")
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    args = parser.parse_args()

    # set grid size
    N_size = N
    if args.N and int(args.N) > 8:
        N_size = int(args.N)

    # set animation update interval
    updateInterval = 10000
    if args.interval:
        updateInterval = int(args.interval)

    # declare grid
    # grid = np.array([])
    sim = Simulation(N_size)
    sim.run()




if __name__ == '__main__':
    main()
