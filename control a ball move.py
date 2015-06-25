#control a ball

import simplegui

#set the parameter
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

#list pos used to store the position of ball center
pos = [WIDTH / 2, HEIGHT / 2]


def keydown(key):
	vel = 4
	if key == simplegui.KEY_MAP['left']:   #使用中括号，而不是小括号
		pos[0] -= vel

	elif key == simplegui.KEY_MAP['right']:
		pos[0] += vel

	elif key == simplegui.KEY_MAP['up']:   #原点在左上角，所以点UP时纵坐标减小
		pos[1] -= vel

	elif key == simplegui.KEY_MAP['down']:
		pos[1] += vel

def draw(canvas):
	canvas.draw_circle(pos, BALL_RADIUS, 2, 'Red','White')

frame = simplegui.create_frame('control ball', WIDTH, HEIGHT)

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)


#usually forget the 括号
frame.start()