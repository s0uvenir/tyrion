import pyglet
from structs3D import *
from test import *

runTests()

window = pyglet.window.Window()

fps = pyglet.clock.ClockDisplay()

@window.event
def on_draw():
	window.clear()
	point = Point(400,200,0)
	point2 = Point(400,250,1)
	point2.setColor(0,50,0)
	point.draw()
	point2.draw()
	
	point.move(255, 200, 0)
	point.setColor(200,200,0)
	point.draw()
	fps.draw()


pyglet.app.run()

