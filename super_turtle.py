import turtle
import time
class Turtle(turtle.Turtle):
	set_actions = set()
	def __init__(self, *, behaviour = None, player = None, speed = 0, maxspeed = 0, curvespeed = 10, acceleration = 0):
		super(Turtle,self).__init__()
		self.speed(-1)
		Turtle.canvas = self.screen._canvas
		turtle.listen()
		self.id = self.turtle._item
		self.behaviour = behaviour
		self.speed = speed
		self.maxspeed = maxspeed
		self.acceleration = acceleration
		self.player = player
		self.curvespeed = curvespeed
		self.setkeys()
		# Turtle.setting = True

	def bind(self, event_type, callback):
		canvas = self.screen._canvas
		item = self.id
		canvas.bind(event_type, callback)
	
	def setkeys(self):
		if self.player == 1:
			self.Up = 'Up'
			self.Down = 'Down'
			self.Left = 'Left'
			self.Right = 'Right'
		if self.player == 2:
			self.Up = 'w'
			self.Down = 's'
			self.Left = 'a'
			self.Right = 'd'

	def keyboard_moviment():
		canvas = Turtle.canvas
		canvas.bind("<KeyPress>", Turtle.keypress)
		canvas.bind("<KeyRelease>", Turtle.keyrelease)

	def move(self):
		# Turtle.setting = False
		canvas = self.screen._canvas
		item = self.turtle._item
		maxspeed = self.maxspeed
		speed = self.speed
		acceleration = self.acceleration
		cs = self.curvespeed
		if self.behaviour == '8-directions':
			for key in Turtle.set_actions.copy():
				if key == self.Up:
					canvas.move(item, 0, -speed)
				if key == self.Down:
					canvas.move(item, 0, speed)
				if key == self.Left:
					canvas.move(item, -speed, 0)
				if key == self.Right:
					canvas.move(item, speed, 0)
		elif self.behaviour == 'car':
			for key in Turtle.set_actions.copy():
				if key == self.Up:
					if self.speed <= maxspeed:
						print(maxspeed)
						self.speed += acceleration
				if key == self.Down:
					if self.speed >= 0:
						self.speed -= acceleration
				if key == self.Left:
					self.left(cs)
				if key == self.Right:
					self.right(cs)
			self.forward(speed)
			# print(self.speed)
		# Turtle.setting = True

	def update():
		Turtle.canvas.update()

	def keypress(event):
		key = event.keysym
		# if Turtle.setting == True:
		Turtle.set_actions.add(key)
		print (Turtle.set_actions)
	def keyrelease(event):
		key = event.keysym
		# if Turtle.setting == True:
		Turtle.set_actions.remove(key)

leo = Turtle(behaviour = 'car', player = 1, maxspeed = 10, acceleration = 0.05, curvespeed = 4)
rafa = Turtle(behaviour = '8-directions', speed = 10, player = 2)
Turtle.keyboard_moviment()
while True:
	leo.move()
	rafa.move()
	Turtle.update()
	# time.sleep(0.1)
