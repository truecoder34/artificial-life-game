# artificial-life-game
Repository with console python implementation of Simple Artificial Life (simplified MAS) and Conway's game of life

### Installation
```
conda create --name <env_name> --file requirements.txt
conda activate <env_name>
```

## Conways Game of Life
See WIKI for detailes abot Conway's Life: https://conwaylife.com/wiki/Gosper_glider_gun
3 Initial State Animations implemented: <br/>
1 randomly turned cells<br/>
```python conwayGameOfLife.py```<br/>
2 Glider<br/>
```python conwayGameOfLife.py  --grid-size 32 --interval 500 --glider```<br/>
3 Gosper<br/>
```python conwayGameOfLife.py  --interval 500 --gosper```<br/>

## Simple Life Realization
### Details and Rules
**Terms**: Feild, Cell, Agent<br/>

![Artificial Life Example](https://raw.githubusercontent.com/truecoder34/artificial-life-game/main/screen.png)

**Agent** - acting model. Has Physical and Mental health. <br/>
Can make 3 actions: Move, Split, Eat
Each Move decrements Mental Health (by 1). Is not renuable
Each Eat action increase Physical Health . (Eat till MAX_PHYSICAL_HEALTH)
Each Split when Physical Health > 0.8 * MAX_PHYSICAL_HEALTH decrements Physical Health<br/>
**Cell** - each cell of field. Has FOOD (Randomly)<br/>
**Field** - 2 dim Cells array<br/>
Should be renewable : per tick 2 foody cells creates randomly (this value can be changed)
