player = PVector(400,380)

def setup():
    size(800,400)

def draw():
    background(32,32,32)
#player
    fill(0,206,0)
    ellipse(player.x,player.y,40,40)
