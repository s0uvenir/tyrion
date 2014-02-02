from structs3D import *

def runTests():
	yes, no = 0, 0
	print "...:Running Tests:..."
	test = test1()
	yes += test[0] 
	no  += test[1]
	print "|     Pass/Fail     |\n|      %s     %s      |" % (yes, no)
	

def test1():
	yes, no = 0, 0
	point1 = Point(1, 1, 1)
	point2 = Point(2, 2, 2)
	vector1 = Vector(3, 3, 3)
	vector2 = Vector(0, 0, 0)

	vector2 = point1.subtractPointFromPoint(point2)

	if vector2.loc == (-1, -1, -1):
		yes += 1
	else:
		print "Failed: subtractPointFromPoint()"
		no += 1

	vector1 = vector1.addVectorToVector(vector2)

	if vector1.loc == (2, 2, 2):
		yes += 1
	else:
		print "Failed: addVectorToVector"
		no += 1

	point1 = point1.addVectorToPoint(vector1)

	if point1.loc == (3, 3, 3):
		yes += 1
	else:
		print "Failed: addVectorToPoint"
		no += 1

	point2 = point2.subtractVectorFromPoint(vector2)
	
	if point2.loc == (3, 3, 3):
		yes += 1
	else:
		print "Failed: subtractVectorFromPoint"
		no += 1

	return yes, no

