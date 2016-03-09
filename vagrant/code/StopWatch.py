# template for "Stopwatch: The Game"

import simplegui

# define global variables
time = 0
numberStops = 0
numberWholeStops = 0
stopped = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = t/600
    t = t%600
    seconds = t/10
    hundredths = t%10
    
    if len(str(seconds)) == 1:
        returnString =  str(minutes) + ":" + "0" + str(seconds) + "." + str(hundredths)  
    elif len(str(seconds)) == 2:
        returnString =  str(minutes) + ":" + str(seconds) + "." + str(hundredths)
    
    
    
    return returnString
    
# define event handlers for buttons; "Start", "Stop", "Reset"


def start_button():
    global stopped
    timer.start()
    stopped = False
    
def stop_button():
    global numberStops, numberWholeStops, stopped
    timer.stop()
    if not stopped:
        numberStops +=1
        
    if time % 10 == 0 and not stopped:
        numberWholeStops += 1
        
    stopped = True
        
    
def reset_button():
    global time, numberStops, numberWholeStops
    time = 0
    numberStops = 0
    numberWholeStops = 0

# define event handler for timer with 0.1 sec interval

def tick():
    global time
    time += 1
    #print time


# define draw handler

def draw(canvas):
    canvas.draw_text(format(time), (250, 250), 50, 'Red')
    canvas.draw_text(str(numberWholeStops) + "/" + str(numberStops), (450, 50), 30, "red" )
    
    
# create frame
frame = simplegui.create_frame('Testing', 500, 500)


# register event handlers

button1 = frame.add_button('start', start_button)
button2 = frame.add_button('stop', stop_button)
button3 = frame.add_button('reset', reset_button)



timer = simplegui.create_timer(100, tick)

frame.set_draw_handler(draw)




# start frame

frame.start()


# Please remember to review the grading rubric
