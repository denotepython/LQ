#control a ball

import simplegui

#set the parameter
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 80

#list pos used to store the position of ball center
pos = [WIDTH / 2, HEIGHT / 2]
vel = [-4.0/6, 5.0/6]


def draw(canvas):
	pos[0] += vel[0]
	pos[1] += vel[1]
	if pos[0] <= BALL_RADIUS:
		vel[0] = -vel[0]
	elif pos[0] + BALL_RADIUS >= (WIDTH - 10):
		vel[0] = -vel[0]
	elif pos[1] <= BALL_RADIUS:
		vel[1] = -vel[1]
	elif pos[1] + BALL_RADIUS >= (HEIGHT - 1) :
		vel[1] = -vel[1]
	canvas.draw_circle(pos, BALL_RADIUS, 2, 'Red','White')

frame = simplegui.create_frame('control ball', WIDTH, HEIGHT)

frame.set_draw_handler(draw)

#usually forget the 括号
frame.start()