# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui

current_key = 5
counter = 0

# Handler for mouse click
def keydown(key):
    global current_key
    if key == simplegui.KEY_MAP['up']:
        current_key *= 2

        print current_key

# Handler to draw on canvas
def keyup(key):
    global current_key, counter
  
    current_key -= 3
    counter += 1
    print current_key,counter
    
def draw(canvas):    
    canvas.draw_text(str(current_key), [150,150], 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# Start the frame animation
frame.start()
