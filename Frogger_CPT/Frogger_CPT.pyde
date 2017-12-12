ball_1 = PVector(200,0)
speed = PVector(0,0)
def setup():
    size(400,700)
    ball_1.x = random(400)
    speed.x = random(5)
    speed.y = random(5)

def draw():
    global ball_1, speed
    background(160,160,160)
    noStroke
#ball_1
    fill(0)
    ball_1 += speed
    ellipse(ball_1.x,ball_1.y,80,80)
    
    if ball_1.x <= 10 or ball_1.x >= 390:
        speed *= -1
#frog    
    fill(0,204,0)
    mouseY = 680
    ellipse(mouseX, mouseY,40,40)
