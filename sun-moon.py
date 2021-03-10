# This program attempts to display the scale of the moon, sun, and earth.
# 1 pixel = 2158.8 miles (diameter of moon)
# distance from earth to moon = 238,900 miles
# distance from earth to sun = 92,328,000 miles
#
# diameter of sun = 865,370 miles
# diameter of earth = 7,917.5 miles
# diameter of moon = 2,158.8 miles
#
# given a moon diameter of 1 pixel,you would need a display 42,769 pixels wide.
# to show the correct scale.

from ezgraphics import GraphicsWindow
win = GraphicsWindow(42768.204,600)
canvas = win.canvas()

canvas.setColor("black")

canvas.drawOval(42768.204,300,3.668,3.668) #earth
canvas.drawOval(42768.204,410.663,1,1) #moon
canvas.drawOval(-300,100,400.857,400.857) #sun

win.wait()