import pyglet
from structs3D import *
from test import *

runTests()

window = pyglet.window.Window()

@window.event
def on_draw():
	window.clear()
	point = Point(400,200,0)
	point2 = Point(400,250,1)
	point.drawPoint()
	point2.drawPoint()

pyglet.app.run()

