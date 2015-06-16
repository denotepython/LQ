# -*- coding: utf-8 -*-
#http://www.codeskulptor.org/#user40_3AKh2gBcX9_1.py
import simplegui
import random

num_range1 = 100
num_range2 = 1000
counter1 = 0       #used to control the times you guess
counter2 = 0

def new_game():
    print 'New game. Range is from 0 to 100 or 0 to 1000, only choose one'
    print 'Now begin the game! choose one button and enter what you guess'

def range100():
    global num_range1    #Remember use the global variable
    num_range1 = random.randrange(1,100)

def range1000():
    global num_range2
    num_range2 = random.randrange(1,1000)

def get_input(guess):
    global num_range1, num_range2,counter1,counter2
    if (num_range1 != 100 and  num_range2 == 1000):
        if  int(guess) < num_range1:      #guess is always 
                                          #given as a string.
            print 'Higher'
            counter1 += 1
        elif int(guess) > num_range1:
            print 'Lower'
            counter1 += 1
        else:
            print 'You Win! What a smart boy!'
            counter1 = 0
            num_range1 = 100          #return to original state
            
        if counter1 > 6:
            counter1 = 0
            num_range1 = 100
            print 'You have no chance!'
            
    elif (num_range2 != 1000 and num_range1 == 100):
        if  int(guess) < num_range2:
            print 'Higher'
            counter2 += 1
        elif int(guess) > num_range2:
            print 'Lower'
            counter2 += 1    
        else:
            print 'You Win! What a smart boy!'
            counter2 = 0
            num_range2 = 1000
            
        if counter2 > 9:
            counter2 = 0
            num_range2 = 1000
            print 'You have no chance!' 
            
    else:
         new_game()          
        
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Guess the number", 200, 200)
frame.add_button("Range is  [0. 100]", range100, 200)
frame.add_button("Range is  [0. 1000]", range1000, 200)
frame.add_input("Enter a guess", get_input, 200)

new_game()

# Start the frame animation
frame.start()

