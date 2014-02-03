import pyglet, time, random, math
from pyglet.window import key
from util import *
from structs3D import *
from test import *

runTests()

width = 800
height = 600
depth = 1

window = pyglet.window.Window(width = width, height = height)
pyglet.gl.glTranslatef(width/2, height/2, 0) #sets origin to 0,0,0
batch = pyglet.graphics.Batch()

def generatePointCloud(numPoints):
	pointCloud = []
	for i in range(numPoints):
		x = random.randrange(-window.width/2, window.width/2)
		y = random.randrange(-window.height/2, window.height/2)
		z = random.randrange(depth)
		point = Point(x,y,z)
		#point.color = (0,0,0)
		pointCloud.append(point)
	return pointCloud


def redrawScreen(window, objects):
	for obj in objects:
		obj.draw()
	

points = generatePointCloud(100)
#redrawScreen(window, points)

@window.event
def on_key_press(symbol, modifiers):
	if symbol == key.D:
		window.clear()
		redrawScreen(window, points)
		pass
	elif symbol == key.A:
		window.clear()
		origin = Point(0,0,0)
		for i in range(len(points)):
			vector = points[i].subtractPointFromPoint(origin)
			points[i].setPointToPoint(origin)
			points[i] = origin.addVectorToPoint(vector.scaleVector(0.5,0.5,0.5))

		redrawScreen(window, points)
		
		#for item in points:
		#	selected = item
		#	vector = item.subtractPointFromPoint(origin)
		#	selected.setPointToPoint(origin)
		#	item = selected.addVectorToPoint(vector.scaleVector(1,1,1))
		#	item.draw()
		#redrawScreen(window, points)

	elif symbol == key.S:
		window.clear()
		origin = Point(0,0,0)
		for i in range(len(points)):
			vector = points[i].subtractPointFromPoint(origin)
			points[i].setPointToPoint(origin)
			points[i] = origin.addVectorToPoint(vector.scaleVector(2.0,2.0,2.0))

		redrawScreen(window, points)
		pass
	elif symbol == key.R:
		window.clear()
		origin = Point(0,0,0)
		for i in range(len(points)):
			vector = points[i].subtractPointFromPoint(origin)
			points[i].setPointToPoint(origin)
			points[i] = origin.addVectorToPoint(vector.rotateVectorXY(15))

		redrawScreen(window, points)
		pass
	else:
		pass

#@window.event
#def on_draw():
#  	window.clear()
	


pyglet.app.run()


#fps = pyglet.clock.ClockDisplay()
#frame_counter = 0

#def update(dt): 
#    global frame_counter
#    
#    frame_counter += 1
#    if frame_counter == 1000:
#       print time.time() - time_start
#        pyglet.app.exit()

#@window.event
#def on_draw():
	#window.clear()
	#point = Point(400,200,0)
	#point2 = Point(400,250,1)
	#point2.setColor(0,50,0)
	#point.draw()
	#point2.draw()
	#glClear(GL_COLOR_BUFFER_BIT)
	#for i in range(500):
	#	point.move(i, 200, 0)
	#	point.setColor(200,i,0)
	
	#	point.draw()

	#vector = Vector(3, 4, 5)
	#vector.rotateVectorXY(90)

#	fps.draw()

	

#time_start = time.time()
#pyglet.clock.schedule_interval(update, 1/60.0) 
#pyglet.app.run()

