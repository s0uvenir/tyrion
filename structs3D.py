import pyglet
import math
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

	def setPointToPoint(self, point):
		self.x = point.x
		self.y = point.y
		self.z = point.z
		self.updateLoc()

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

	def rotateVectorXY(self, degree):
		degree = math.radians(degree)
		vector = self
		a0,a1,a2 = vector.x, vector.y, vector.z

		b0 = (math.cos(degree)*a0) + (-math.sin(degree)*a1) + 0*a2
		b1 = (math.sin(degree)*a0) + (math.cos(degree)*a1) + 0*a2
		b2 = 0*a0 + 0*a1 + 1*a2

		vector.x = b0
		vector.y = b1
		vector.z = b2
		vector.updateLoc()

		return vector

	def rotateVectorXZ(self, degree):
		degree = math.radians(degree)
		vector = self
		a0,a1,a2 = vector.x, vector.y, vector.z

		b0 = (math.cos(degree)*a0) + 0*a1 + (math.sin(degree)*a2)
		b1 = 0*a0 + 1*a1 + 0*a2
		b2 = (-math.sin(degree)*a0) + 0*a1 + (math.cos(degree)*a2)

		vector.x = b0
		vector.y = b1
		vector.z = b2
		vector.updateLoc()

		return vector

	def rotateVectorYZ(self, degree):
		degree = math.radians(degree)
		vector = self
		a0,a1,a2 = vector.x, vector.y, vector.z

		b0 = 1*a0 + 0*a1 + 0*a2
		b1 = 0*a0 + (math.cos(degree)*a1) + (-math.sin(degree)*a2)
		b2 = 0*a0 + (math.sin(degree)*a1) + (math.cos(degree)*a2)

		vector.x = b0
		vector.y = b1
		vector.z = b2
		vector.updateLoc()

		return vector
	
	def scaleVector(self, s0, s1, s2):
		vector = self
		vector.x *= s0
		vector.y *= s1
		vector.z *= s2
		vector.updateLoc()
		return vector

	def updateLoc(self):
		self.loc = (self.x, self.y, self.z)
	
