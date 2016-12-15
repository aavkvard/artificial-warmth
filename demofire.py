#!/usr/bin/sudo python3

import time
import random

import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(180)
unicorn.brightness(.8)
u_width,u_height=unicorn.get_shape()

palette = [
	(0x00,0x00,0x00),
	(0x00,0x00,0x00),
	(0x00,0x00,0x00),
	(0x45,0x00,0x00),
	(0x5d,0x1a,0x00),
	(0x83,0x25,0x00),
	(0xb3,0x3e,0x00),
	(0xed,0x7d,0x00),
	(0xfc,0xad,0x00),
	(0xff,0xc6,0x36),
]

board = [[0 for i in range(8)] for j in range(8)]
pattern = [[-1,-1],[0,-1],[1,-1],[0,0]]

def getavg(x,y):
    colorsum = 0
    for i in range(len(pattern)):
        (tx, ty) = (x+pattern[i][0], y+pattern[i][1])
        if tx>(len(board)-1):
            tx = tx-(len(board)-1)
        elif tx < 0:
            tx = (len(board)-1)+tx
        colorsum += board[tx][ty]
    coloravg = colorsum//(len(pattern))
    return coloravg

while True:

    board[random.randrange(8)][0] = random.randrange(1)+7
    board[random.randrange(8)][0] = random.randrange(2)+2

    for y in range(1,u_height):
        for x in range(u_width):
            board[x][y] = getavg(x,y)

    for y in range(u_height):
        for x in range(u_width):
            (r, g, b) = palette[board[x][y]]
            unicorn.set_pixel(x, y, r, g, b)

    unicorn.show()

    time.sleep(0.01)

