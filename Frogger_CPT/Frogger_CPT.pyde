frog = PVector(410,357)

key_states = []
for _ in range(223):
    key_states.append(False)

def setup():
    size(800,400)

def draw():
    background(32,32,32)
#player
    fill(0,206,0)
    rect(frog.x,frog.y,40,40)
#movement        
    if key_states[37]:  # left
        frog.x -= 1
    elif key_states[39]:  # right
        frog.x += 1
    if key_states[38]:  # up
        frog.y -= 1
    elif key_states[40]:  # down
        frog.y += 1
        
def keyPressed():
    global key_states
    key_states[keyCode] = True
    
    
def keyReleased():
    global key_states
    key_states[keyCode] = False
        
