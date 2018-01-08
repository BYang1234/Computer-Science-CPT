frog = PVector(310,657)
car_1 = PVector(100, 600)
car_2 = PVector(-100, 600)
car_3 = PVector(-300, 600)
car_4 = PVector(0, 500)
car_5 = PVector(-200, 500)
car_6 = PVector(-400, 500)
car_7 = PVector(50, 400)
car_8 = PVector(-200, 400)
speed_1 = 1.2
speed_2 = 2
speed_3 = 2.5


key_states = []
for _ in range(223):
    key_states.append(False)

def setup():
    size(600,700)

def draw():
    global frog, car_1, car_2, car_3, car_4, car_5, car_6, speed_1, speed_2, speed_3
    background(32,32,32)

#player
    fill(0,206,0)
    rect(frog.x,frog.y,40,40)
    if frog.y >= height:
        frog.y = 657
        frog.x = 310
    if frog.x <= 0 or frog.x >= 600:
        frog.x = 310
        frog.y = 657
    
#car 1
    fill(143,7,12)
    car_1.x += speed_1
    rect(car_1.x,car_1.y,60,40)
    if car_1.x > width:
        car_1.x = 10

#car 2 
    fill(143,7,12)
    car_2.x += speed_1
    rect(car_2.x, car_2.y, 60, 40)
    if car_2.x > width:
        car_2.x = 10

#car 3    
    fill(143,7,12)
    car_3.x += speed_1
    rect(car_3.x,car_3.y,60,40)
    if car_3.x > width:
        car_3.x = 10

#car 4 
    fill(225,225,0)
    car_4.x += speed_2
    rect(car_4.x, car_4.y, 60,40)
    if car_4.x > width:
        car_4.x = 10

#car 5 
    fill(225,225,0)
    car_5.x += speed_2
    rect(car_5.x, car_5.y, 60,40)
    if car_5.x > width:
        car_5.x = 10

#car 6
    fill(225,225,0)
    car_6.x += speed_2
    rect(car_6.x, car_6.y, 60,40)
    if car_6.x > width:
        car_6.x = 10

#car 7
    fill(225)
    car_7.x += speed_3
    rect(car_7.x, car_7.y, 40,40)
    if car_7.x > width:
        car_7.x = 10

#car 8
    fill(225)
    car_8.x += speed_3
    rect(car_8.x, car_8.y, 40,40)
    if car_8.x > width:
        car_8.x = 10

    
#middle safeground
    fill(225,100)
    rect(0, height/2, 600, 40)

#river 
    fill(59, 179, 208)
    rect(0, height/7, 600, 250)

#end zone
    fill(225,100)
    rect(0, height/150, 600, 100)

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
