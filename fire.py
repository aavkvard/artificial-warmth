#!/usr/bin/env python

import time
import random

import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(180)
unicorn.brightness(.8)
u_width,u_height=unicorn.get_shape()

palette = [
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

while True:

    board[random.randrange(8)][0] = random.randrange(1)+6
    board[random.randrange(8)][random.randrange(1)] = random.randrange(3)+3

    for y in range(1,u_height):
        for x in range(u_width):
            tx = (x-1)+random.randrange(2)
            if tx>7:
                tx = tx-7
            elif tx < 0:
                tx = 7+tx
            if board[tx][y-1] > 0:
                board[x][y] = board[tx][y-1]-1

    for y in range(u_height):
        for x in range(u_width):
            (r, g, b) = palette[board[x][y]]
            unicorn.set_pixel(x, y, r, g, b)

    unicorn.show()

    time.sleep(0.05)

