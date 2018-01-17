from Car import Car
from Frog import Frog


car_list = [Car(100, 600, 1.2), Car(-100, 600, 1.2), Car(-300, 600, 1.2), Car(0, 500, 1.75), Car(-200, 500, 1.75), Car(-400, 500, 1.75), Car(50, 400, 2.75), Car(-200, 400, 2.75), Car(0, 300, 2.25), Car(-300, 300, 2.25), Car(100, 200, 1.5), Car(-100, 200, 1.5), Car(-300, 200, 1.5), Car(0, 100, 4)]
frog = Frog(310, 657)

key_states = []
for _ in range(223):
    key_states.append(False)


def setup():
    size(600, 700)

def intersect(car, frog):
    if car.location.x > (frog.location.x + frog.width) or (car.location.x + car.width) < frog.location.x:
        return False
    if car.location.y > (frog.location.y + frog.height) or (car.location.y + car.height) < frog.location.y:
        return False
    return True

def draw():
    global car_list, frog
    background(32, 32, 32)

        
#writing
    fill(255,255,0)
    textSize(30)
    text("Frogger", 50, 50)

#frog and cars
    frog.draw()
    frog.move(key_states)
    
    if frog.location.y >= height:
        frog.resetGame()
    if frog.location.x <= 0 or frog.location.x >= 600:
        frog.resetGame()    

    for car in car_list:
        car.move()
        car.draw()
        if intersect(car, frog):
            frog.resetGame()
        if frog.location.y <= 60:
            frog.endGame()

#Reset game after winning    
        if mousePressed == True:
            frog.resetGame()                
#end zone
    fill(225, 100)
    rect(0, 0, 600, 100)


def keyPressed():
    global key_states
    key_states[keyCode] = True
    

def keyReleased():
    global key_states
    key_states[keyCode] = False
    
