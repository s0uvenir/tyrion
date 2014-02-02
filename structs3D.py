import pyglet
from pyglet.gl import *

class Point():
	def __init__ (self, x, y, z):
		self.x	 = 	x
		self.y	 =	y
		self.z	 =	z
		self.loc = 	(x, y, z)
		self.color = 	(255, 255, 255)	
	
	def addVectorToPoint(self, vector):
		point = Point(self.x + vector.x, self.y + vector.y, self.z + vector.z)
		return point
		
	def subtractVectorFromPoint(self, vector):
		point = Point(self.x - vector.x, self.y - vector.y, self.z - vector.z)
		return point
		
	def subtractPointFromPoint(self, point):
		vector = Vector(self.x - point.x, self.y - point.y, self.z - point.z)
		return vector

	def updateLoc(self):
		self.loc = (self.x, self.y, self.z)

	def setColor(self, r, g, b):
		self.color = (r, g, b)

	def move(self, x, y, z):
		self.x	 = 	x
		self.y	 =	y
		self.z	 =	z
		self.updateLoc()

	def draw(self):
		vertexList = pyglet.graphics.vertex_list(1, 
			('v3i', self.loc),
			('c3B', self.color))
		vertexList.draw(pyglet.gl.GL_POINTS)

class Color():
	def __init__ (self, r, g, b):
		self.r 	=	r
		self.g	=	g
		self.b	=	b	
		
class Vector():
	def __init__ (self, x, y, z):
		self.x	=	x
		self.y	=	y 
		self.z	=	z
		self.loc = (x, y, z)

	def addVectorToVector(self, vector):
		vector = Vector(self.x + vector.x, self.y + vector.y, self.z + vector.z)
		return vector
		
	def subtractVectorFromVector(self, vector):
		vector = Vector(self.x - vector.x, self.y - vector.y, self.z - vector.z)
		return vector

	def updateLoc(self):
		self.loc = (self.x, self.y, self.z)
	
