# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
paddle2_pos = [WIDTH - HALF_PAD_WIDTH -1, HEIGHT/2]
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
UP1 = False
UP2 = False
DOWN1 = False
DOWN2 = False
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
acc = 2
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def restart():
    global score1, score2
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[0] = 2 * random.random()
    ball_vel[1] = 2 * random.random()
    score1 = 0
    score2 = 0
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists


# define event handlers
def new_game():
      # these are numbers
    global score1, score2  # these are ints

def draw(canvas):
    global score1, score2
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_text(str(score1) + ':' +str(score2), (WIDTH/2 - 20, 20), 30, 'Red' )   
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[0] <= BALL_RADIUS + HALF_PAD_WIDTH:
        ball_vel[0] = -ball_vel[0]
    elif ball_pos[0] + BALL_RADIUS + HALF_PAD_WIDTH >= (WIDTH - 1):
        ball_vel[0] = -ball_vel[0]
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] + BALL_RADIUS >= (HEIGHT - 1) :
        ball_vel[1] = -ball_vel[1] 
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'Red', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    paddle1_pos[1] += paddle1_vel
    paddle2_pos[1] += paddle2_vel
    canvas.draw_polygon([[paddle1_pos[0]-HALF_PAD_WIDTH, paddle1_pos[1]-HALF_PAD_HEIGHT],\
                         [paddle1_pos[0]+HALF_PAD_WIDTH, paddle1_pos[1]-HALF_PAD_HEIGHT-1],\
                         [paddle1_pos[0]+HALF_PAD_WIDTH, paddle1_pos[1]+HALF_PAD_HEIGHT-1],\
                         [paddle1_pos[0]-HALF_PAD_WIDTH, paddle1_pos[1]+HALF_PAD_HEIGHT]],\
                         1,'White', 'White')
    canvas.draw_polygon([[paddle2_pos[0]-HALF_PAD_WIDTH, paddle2_pos[1]-HALF_PAD_HEIGHT],\
                         [paddle2_pos[0]+HALF_PAD_WIDTH, paddle2_pos[1]-HALF_PAD_HEIGHT-1],\
                         [paddle2_pos[0]+HALF_PAD_WIDTH, paddle2_pos[1]+HALF_PAD_HEIGHT-1],\
                         [paddle2_pos[0]-HALF_PAD_WIDTH, paddle2_pos[1]+HALF_PAD_HEIGHT]],\
                         1,'White', 'White')
    
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel, acc,UP1, UP2, DOWN1, DOWN2
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= acc
        UP1 = True
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel += acc
        DOWN1 = True
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel -= acc
        UP2 = True
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel += acc
        DOWN2 = True

def keyup(key):
    global paddle1_vel, paddle2_vel, acc, UP1, UP2, DOWN1, DOWN2
    if UP1 == True:
        paddle1_vel += acc
        UP1 = False
    if DOWN1 == True:
        paddle1_vel -= acc
        DOWN1 = False
    if UP2 == True:
        paddle2_vel += acc
        UP2 = False
    if DOWN2 == True:
        paddle2_vel -= acc
        DOWN2 = False


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
restart = frame.add_button('Restart', restart)

# start frame
new_game()
frame.start()

