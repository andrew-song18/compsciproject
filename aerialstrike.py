#player setup over spring break through turtle
#week 1: set up of turtle and user control
#week 2: tijuana immersion, didn't really work on code as much as I would have wanted to
#week 3: create boundaries detection and draw borders, initial listening of keyboard
#week 4: defined collision if turtle hits boundaries. Created github repository. Created missile class
#week 4 cont: having hard time with user detecting collision with missile class.



import random
import turtle

turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht() #LINE CREDITED TO STACK OVERFLOW for effective Turtle setup
turtle.tracer(1)

class Player(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape) 
		self.speed(0)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.speed = 1 #regular setting, might change later

class Missile(sprite):
	def __init__(self, spriteshape, color, startx, starty):
		sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 10
		self.setheading(random.randint(0,360))	
		

#Create player to start working
player = Player("triangle", "white", 0, 0) 
missile = Missile("circle", "red", -100, 0)
#triangle is temporary until we link to different object for player control - like a photo of man through bird's eyes view
		
#defining boundaries detection through cartesian plane. We want a square plane.
	
def move(self):
		self.fd(self.speed)
		
		
		if self.xcor() > 500:
			self.setx(500)
			self.rt(60)
		
		if self.xcor() < -500:
			self.setx(-500)
			self.rt(60)
		
		if self.ycor() > 500:
			self.sety(500)
			self.rt(60)
		
		if self.ycor() < 500:
			self.sety(-500)
			self.rt(60)

def draw_border(self):
		#Draw border
		self.pen.speed(0)
		self.pen.color("black")
		self.pen.pensize(3)
		self.pen.penup()
		self.pen.goto(-500, 500)
		self.pen.pendown()
		for side in range(4):
			self.pen.fd(600)
			self.pen.rt(90)
		self.pen.penup()
		self.pen.ht()

def is_collision(self, other):
		if (self.xcor() >= (other.xcor() - 50)) and \
		(self.xcor() <= (other.xcor() + 50)) and \
		(self.ycor() >= (other.ycor() - 50)) and \
		(self.ycor() <= (other.ycor() + 50)):
			return True
		else:
			return False

#Initialize the drawing of the game border
game.draw_border()

#Key listening, functions found online in stackoverflow dictionary
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.listen()

#necessary game loop
while True:
	player.move()


