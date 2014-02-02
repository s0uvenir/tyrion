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
batch = pyglet.graphics.Batch()
	
def generatePointCloud(numPoints):
	pointCloud = []
	for i in range(numPoints):
		x = random.randrange(window.width)
		y = random.randrange(window.height)
		z = random.randrange(depth)
		point = Point(x,y,z)
		#point.color = (0,0,0)
		pointCloud.append(point)
	return pointCloud

points = generatePointCloud(100)

@window.event
def on_key_press(symbol, modifiers):
	if symbol == key.D:
		window.clear()
		pass
	elif symbol == key.A:
		origin = Point(0,0,0)
		for item in points:
			#vector = item.subtractPointFromPoint(origin)
			#item.setPointToPoint(origin)
			item.addVectorToPoint(vector.scaleVector(0.5,0.5,0.5))
	elif symbol == key.S:
		pass
	elif symbol == key.R:
		pass
	else:
		pass

@window.event
def on_draw():
    	window.clear()
	for item in points:
		item.draw()




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

