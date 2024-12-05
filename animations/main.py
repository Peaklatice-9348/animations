import pgzrun
from random import randint
import itertools
WIDTH = 400
HEIGHT = 400
block_positions = [(350,50),(350,350),(50,350),(50,50)]
b_pos = itertools.cycle(block_positions)

block = Actor('metal_block',center =(50,50))

def draw():
    screen.clear()
    block.draw()


pgzrun.go()