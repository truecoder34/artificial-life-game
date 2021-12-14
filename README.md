# artificial-life-game
Repository with console python implementation of Simple Artificial Life (simplified MAS) and Conway's game of life

### Installation
'''
conda create --name <env_name> --file requirements.txt
conda activate <env_name>
'''

## Conways Game of Life
See WIKI for detailes abot Conway's Life: https://conwaylife.com/wiki/Gosper_glider_gun
3 Initial State Animations implemented:
1 - randomly turned cells
'''python conwayGameOfLife.py'''
2 - Glider
'''python conwayGameOfLife.py  --grid-size 32 --interval 500 --glider'''
3 - Gosper
'''python conwayGameOfLife.py  --interval 500 --gosper'''

## Simple Life Realization
### Details and Rules
Terms: Feild, Cell, Agent
1 - Agent - acting model. Has Physical and Mental health. 
	Can make 3 actions: Move, Split, Eat
	Each Move decrements Mental Health (by 1). Is not renuable
	Each Eat action increase Physical Health . (Eat till MAX_PHYSICAL_HEALTH)
	Each Split when Physical Health > 0.8 * MAX_PHYSICAL_HEALTH decrements Physical Health
2 - Cell - each cell of field. Has FOOD (Randomly)
3 - Field - 2 dim Cells array. 
	Should be renuable . (Not implementedted)