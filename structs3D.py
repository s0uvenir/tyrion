class Point():
	def __init__ (self, x, y, z):
		self.x	 = 	x
		self.y	 =	y
		self.z	 =	z
		self.loc = 	(x, y, z)
	
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

	def drawPoint(self, canvas):
		
		print self.loc
		
		
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
	
