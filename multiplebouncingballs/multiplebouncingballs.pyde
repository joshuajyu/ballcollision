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
    
    def checkCollision(self, otherball):
        distance = PVector.sub(otherball.position, self.position)
        distanceMag = distance.mag()
        minDistance = self.radius + otherball.radius
        print(distanceMag)
        if distanceMag < minDistance:
            distanceCorrection = (minDistance - distanceMag)/2
            d = distance.copy()
            correctionVector = d.normalize().mult(distanceCorrection)
            otherball.position.add(correctionVector)
            self.position.sub(correctionVector)
            theta = distance.heading()
            sine = sin(theta)
            cosine = cos(theta)
            bTemp = [PVector(), PVector()]
            bTemp[1].x = cosine * distance.x + sine * distance.y
            bTemp[1].y = cosine * distance.y - sine * distance.x
            tempVec = [PVector(), PVector()]
            tempVec[0].x = cosine * self.velocity.x + sine * self.velocity.y
            tempVec[0].y = cosine * self.velocity.y - sine * self.velocity.x
            tempVec[1].x = cosine * otherball.velocity.x + sine * otherball.velocity.y
            tempVec[1].y = cosine * otherball.velocity.y - sine * otherball.velocity.x
            finalVec = [PVector(), PVector()] 
            finalVec[0].x = ((self.m - otherball.m) * tempVec[0].x + 2 * otherball.m *tempVec[1].x) / (self.m + otherball.m)
            finalVec[0].y = tempVec[1].y   
            finalVec[1].x = ((otherball.m - self.m) * tempVec[1].x + 2 * self.m *tempVec[0].x) / (self.m + otherball.m)
            finalVec[1].y = tempVec[1].y 
            bTemp[0].x += finalVec[0].x     
            bTemp[1].x += finalVec[1].x 
            bFinal = [PVector(), PVector()]
            bFinal[0].x = cosine * bTemp[0].x - sine * bTemp[0].y
            bFinal[0].y = cosine * bTemp[0].y + sine * bTemp[0].x
            bFinal[1].x = cosine * bTemp[1].x - sine * bTemp[1].y
            bFinal[1].y = cosine * bTemp[1].y + sine * bTemp[1].x
            otherball.position.x = self.position.x + bFinal[1].x
            otherball.position.y = self.position.y + bFinal[1].y
            self.position.add(bFinal[0])
            self.velocity.x = cosine * finalVec[0].x - sine * finalVec[0].y
            self.velocity.y = cosine * finalVec[0].y + sine * finalVec[0].x
            otherball.velocity.x = cosine * finalVec[1].x - sine * finalVec[1].y
            otherball.velocity.y = cosine * finalVec[1].y + sine * finalVec[1].x
            
balls = [Ball(100, 400, 20), Ball(700, 400, 80)]

def draw():
    background(51)
    for x in range(len(balls)):
        balls[x].update()
        balls[x].display()
        balls[x].checkBoundaryCollision()
    balls[0].checkCollision(balls[1])
    print("checked")
        
