#!/usr/bin/sudo python3

import time
import random

try:
    import unicornhat as unicorn
except ImportError:
    from unicorn_hat_sim import unicornhat as unicorn
    #unicorn.rotation(180)


unicorn.set_layout(unicorn.AUTO)
#unicorn.rotation(180)
unicorn.brightness(.8)
u_width,u_height=unicorn.get_shape()

def create_palette(fromcolor,tocolor,steps):
    rstep = (tocolor[0] - fromcolor[0]) / steps
    gstep = (tocolor[1] - fromcolor[1]) / steps
    bstep = (tocolor[2] - fromcolor[2]) / steps
    r = fromcolor[0]
    g = fromcolor[1]
    b = fromcolor[2]
    palette = []
    for x in range(steps):
        palette += [(int(r),int(g),int(b))]
        r += rstep
        g += gstep
        b += bstep
    return palette

palette = create_palette((0x30,0x00,0x00),(0xff,0xc6,0x26),u_height)

# a static palette for the standard Unicorn Hat
#palette = [
#	(0x00,0x00,0x00),
#	(0x00,0x00,0x00),
#	(0x00,0x00,0x00),
#	(0x45,0x00,0x00),
#	(0x5d,0x1a,0x00),
#	(0x83,0x25,0x00),
#	(0xb3,0x3e,0x00),
#	(0xed,0x7d,0x00),
#	(0xfc,0xad,0x00),
#	(0xff,0xc6,0x36),
#]

board = [[0 for i in range(u_height)] for j in range(u_width)]
pattern = [[-1,-1],[0,-1],[1,-1],[0,0]]

def getavg(x,y):
    colorsum = 0
    for i in range(len(pattern)):
        (tx, ty) = (x+pattern[i][0], y+pattern[i][1])
        if tx>(len(board)-1):
            tx = tx-(len(board)-1)
            ty = u_height-1
        elif tx < 0:
            tx = (len(board)-1)+tx
            ty = u_height-1
        colorsum += board[tx][ty]
    coloravg = colorsum//(len(pattern))
    return coloravg


while True:

    board[random.randrange(len(board))][0] = u_height-1
    board[random.randrange(len(board))][0] = random.randrange(u_height//2)+u_height//4
    board[random.randrange(len(board))][0] = random.randrange(u_height//2)+u_height//5

    for y in range(1, u_height):
        for x in range(u_width):
            board[x][y] = getavg(x,y)

    for y in range(u_height):
        for x in range(u_width):
            (r, g, b) = palette[board[x][y]]
            unicorn.set_pixel(x, y, r, g, b)

    unicorn.show()
    time.sleep(0.01)

