#multiple bouncing balls

def setup():
    size(640, 360)

class Ball:
    global velocity, position
    position = PVector
    velocity = PVector
    radius = 0.0
    m = 0.0
    def __init__(self, x, y, r):
        self.position = PVector(x, y)
        self.velocity = PVector.random2D()
        self.velocity.mult(3)
        self.radius = r
        self.m = self.radius*0.1
        
    def update(self):
        self.position.add(velocity)
    
    def checkBoundaryCollision():
        if position.x > width-radius:
            position.x = width-radius
            velocity.x *= -1
        elif position.x < radius:
            position.x = radius
            velocity.x *= -1
        elif position.y > height-radius:
            position.y = height-radius
            velocity.y *= -1
        elif position.y > radius:
            position.y = radius
            velocity.y *= -1

balls = [Ball(100, 400, 20), Ball(700, 400, 80)]
def draw():
    background(0)
    for x in range(len(balls)):
        balls[x].update()
        balls[x].checkBoundaryCollision

        
