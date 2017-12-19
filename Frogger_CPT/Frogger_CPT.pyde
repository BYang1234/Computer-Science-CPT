frog = PVector(410,357)
car_1 = PVector(0, 300)
car_2 = PVector(-150, 300)
speed = 2

key_states = []
for _ in range(223):
    key_states.append(False)

def setup():
    size(600,400)

def draw():
    background(32,32,32)
#player
    fill(0,206,0)
    rect(frog.x,frog.y,40,40)
#car 1
    fill(255)
    car_1.x += speed
    rect(car_1.x,car_1.y,60,40)
    if car_1.x > width:
        car_1.x = 0

#car 2 
    fill(255)
    car_2.x += speed
    rect(car_2.x, car_2.y, 60, 40)
    if car_2.x > width:
        car_2.x = 0
            
    
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
        
