frog = PVector(310,357)
car_1 = PVector(100, 300)
car_2 = PVector(-100, 300)
car_3 = PVector(-300, 300)
speed = 1.5

key_states = []
for _ in range(223):
    key_states.append(False)

def setup():
    size(600,400)

def draw():
    global frog, car_1, car_2, speed
    background(32,32,32)
#player
    fill(0,206,0)
    rect(frog.x,frog.y,40,40)
    if frog.y >= height:
        frog.y = 357
        frog.x = 310
    if frog.x <= 0 or frog.x >= 600:
        frog.x = 310
        frog.y = 357
    
#car 1
    fill(255)
    car_1.x += speed
    rect(car_1.x,car_1.y,60,40)
    if car_1.x > width:
        car_1.x = 10

#car 2 
    fill(255)
    car_2.x += speed
    rect(car_2.x, car_2.y, 60, 40)
    if car_2.x > width:
        car_2.x = 10

#car 3    
    fill(255)
    car_3.x += speed
    rect(car_3.x,car_3.y,60,40)
    if car_3.x > width:
        car_3.x = 10
            
    
#movement        
    if key_states[37]:  # left
        frog.x -= 2
    elif key_states[39]:  # right
        frog.x += 2
    if key_states[38]:  # up
        frog.y -= 2
    elif key_states[40]:  # down
        frog.y += 2
        
def keyPressed():
    global key_states
    key_states[keyCode] = True
    
    
def keyReleased():
    global key_states
    key_states[keyCode] = False
