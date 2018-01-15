from Car import Car
from Frog import Frog


car_list = [Car(100, 600, 1.2), Car(-100, 600, 1.2), Car(-300, 600, 1.2), Car(0, 500, 2), Car(-200, 500, 2), Car(-400, 500, 2), Car(50, 400, 2.75), Car(-200, 400, 2.75), Car(0, 300, 2.25), Car(-300, 300, 2.25), Car(100, 200, 1.5), Car(-100, 200, 1.5), Car(-300, 200, 1.5), Car(0, 100, 5)]
frog = Frog(310, 657)

key_states = []
for _ in range(223):
    key_states.append(False)


def setup():
    size(600, 700)


def draw():
    global car_list, frog
    background(32, 32, 32)

        
#writing
    fill(255,255,0)
    textSize(30)
    text("Frogger", 50, 50)

    frog.draw()
    frog.resetGame()
    frog.move(key_states)
    frog.endGame()

    for car in car_list:
        car.move()
        car.draw()
        
#end zone
    fill(225, 100)
    rect(0, 0, 600, 100)


def keyPressed():
    global key_states
    key_states[keyCode] = True
    

def keyReleased():
    global key_states
    key_states[keyCode] = False
