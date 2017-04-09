'''
generate_arc.py

Purpose:
	Draws a series of lines along an arc toward the centre of the canvas, in
	a line format for an svg converter.

Use:
	Pass the following parameters in the following order via stdin:
	x0	the x position of the outtermost end of the first line
	y0	the y position of the outtermost end of the first line
	x1	the x position of the innermost end of the first position
	y1	the y position of the innermost end of the first line
	dtheta0	the absolute rotation (radians) of the first rotate operation
	ql	the scaling factor for the line defined by [[x0, y0], [x1, y1]]
	qtheta	the arc rate: where theta is the angle coordinate defined by
		qtheta = theta_n/theta{n-1} for all lines
	n	the number of lines
	colour	the colour of all lines

Preconditions:
	No lines defined by the parameters lie outside the canvas.
'''

import sys
import math
import Line_Point_colour

'''
Purpose:
	Draws a series of shrinking or growing lines along an arc toward the
	centre of the canvas through line files for an svg converter.

	line is of type line as defined in Line_point.py
	theta is the number of radians the original line will be rotated by
	n is the number of lines left
	
Preconditions:
	No lines defined by the parameters lie outside the canvas, and there is	
	enough dynamic memory available.
'''
def recursive_draw(l, theta, n):
	print 'line', l
	if n == 0:
		return
	else:
		#Transform the line
		l.rotate(theta)
		l.scale(ql)

		#recurse
		recursive_draw(l, theta*qtheta, n-1)

# process the command line arguments
x0 = float(sys.argv[1])
y0 = float(sys.argv[2])
x1 = float(sys.argv[3])
y1 = float(sys.argv[4])
dtheta = float(sys.argv[5])
ql = float(sys.argv[6])
qtheta = float(sys.argv[7])
n = int(sys.argv[8])
colour = str(sys.argv[9])

#derive initial vertices
v0 = Line_Point_colour.Point(x0, y0)
v1 = Line_Point_colour.Point(x1, y1)


#derive first line
l0 = Line_Point_colour.Line(v0, v1, colour)

#recursively print the lines
recursive_draw(l0, dtheta, n)
