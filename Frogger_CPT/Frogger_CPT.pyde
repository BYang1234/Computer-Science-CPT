ffrog = PVector(410,357)

def setup():
    size(800,400)

def draw():
    background(32,32,32)
#player
    fill(0,206,0)
    rect(frog.x,frog.y,40,40)
#movement        
    
def move_left():
    x -= 1
    frog.x(x)

def move_right():
    x += 1    
    frog.x(x)
    
def move_up():
    y += 1
    frog.y(y)
    
def move_down():
    y -= 1
    frog.y(y)
        
