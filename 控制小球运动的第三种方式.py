#control a ball

import simplegui

#set the parameter
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 80
acc = 1
LEFT = 0
RIGHT = 0
UP = 0
DOWN = 0
#list pos used to store the position of ball center
pos = [WIDTH / 2, HEIGHT / 2]
vel = [0, 0]


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

def keydown(key):
	global acc, LEFT, RIGHT, UP, DOWN
	if key == simplegui.KEY_MAP['left']:   #使用中括号，而不是小括号
		vel[0] -= acc
		LEFT = 1

	elif key == simplegui.KEY_MAP['right']:
		vel[0] += acc
		RIGHT = 1

	elif key == simplegui.KEY_MAP['up']:   #原点在左上角，所以点UP时纵坐标减小
		vel[1] -= acc
		UP = 1

	elif key == simplegui.KEY_MAP['down']:
		vel[1] += acc
		DOWN = 1

def keyup(key):
	global acc, LEFT, RIGHT, UP, DOWN
	if LEFT == 1:
		vel[0] += acc
		LEFT = 0
	elif RIGHT == 1:
		vel[0] -= acc
		RIGHT = 0
	elif UP == 1:
		vel[1] += acc
		UP = 0
	elif DOWN == 1:
		vel[1] -= acc
		DOWN = 0


frame = simplegui.create_frame('control ball', WIDTH, HEIGHT)

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

#usually forget the 括号
frame.start()