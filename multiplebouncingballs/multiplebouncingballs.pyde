#multiple bouncing balls

def setup():
    size(640, 360)

class Ball:
    global velocity, position, radius
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
        self.position.add(self.velocity)
    
    def checkBoundaryCollision(self):
        if self.position.x > width-self.radius:
            self.position.x = width-self.radius
            self.velocity.x *= -1
        elif self.position.x < self.radius:
            self.position.x = self.radius
            self.velocity.x *= -1
        elif self.position.y > height-self.radius:
            self.position.y = height-self.radius
            self.velocity.y *= -1
        elif self.position.y < self.radius:
            self.position.y = self.radius
            self.velocity.y *= -1
            
    def display(self):
        noStroke()
        fill(204)
        ellipse(self.position.x, self.position.y, self.radius*2, self.radius*2)
        
balls = [Ball(100, 400, 20), Ball(700, 400, 80)]

def draw():
    background(51)
    for x in range(len(balls)):
        balls[x].update()
        print("updated")
        balls[x].display()
        print("displayed")
        balls[x].checkBoundaryCollision()
        print("checked")

        
