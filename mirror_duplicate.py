'''
mirror_duplicate.py

Purpose:
	Prints via stdout: the contents of a lines file, which may be mirrored
	about the x, y, or x and y planes, as well as a version rotated about
	the origin a number of times. The rotation feature is like making a copy
	and rotating it 2*pi/n radians n-1 times.

Use:
	Pass the following via stdin in the following order:

	file_name.extension	The lines file
	planes			The plane(s) to mirror about: one of:
				{none, x, y, xy}
	n			The number of rotations.
'''

import sys
import copy
import math
import Line_Point_colour

'''
print_lines(L)

Purpose:
	Takes a list of two x-y coordinate pairs, and prints them to stdout such that
	they may be converted to svg format by another program.
	
Preconditions:
	L is a list of two x-y coordinate pairs, and nothing else.
'''
def print_lines(L):
	for lines in L:
		print 'line', lines
	return
	
'''
mirror_y(L)

Purpose:
	Takes a list of line objects as defined in Line_Point.py, and appends a list of
	equal length, where each x coordinate has been replaced with it's negative.
	
Preconditions:
	L is of type list, and contains only line objects created with the Line_point.py module.
'''
def mirror_y(L):
	M = []
	for lines in L:
		l = Line_Point_colour.Line(lines.point0, lines.point1, lines.colour)
		l.point0.x *= -1
		l.point1.x *= -1
		M.append(l)
	for lines in M:
		L.append(lines)
	return

'''
mirror_x(L)

Purpose:
	Takes a list of line objects as defined in Line_Point.py, and appends a list of
	equal length, where each y coordinate has been replaced with it's negative.
	
Preconditions:
	L is of type list, and contains only line objects created with the Line_point.py module.
'''
def mirror_x(L):
	M = []
	for lines in L:
		l = Line_Point_colour.Line(lines.point0, lines.point1, lines.colour)
		l.point0.y *= -1
		l.point1.y *= -1
		M.append(l)
	for lines in M:
		L.append(lines)
	return
	
'''
rotate_copy(n)

Purpose:
	Takes a list of line objects as defined in Line_Point.py, and makes copies
	rotated in increments of 2*pi/n radians.
	
Preconditions:
	L is of type list, and contains only line objects created with the Line_point.py module.
	Rads is at least zero (this is a paranoid precondition)
'''
def rotate_copy(L, rads):
	M = []
	for lines in L:
		l = Line_Point_colour.Line(lines.point0, lines.point1, lines.colour)
		l.rotate(rads)
		M.append(l)
	for lines in M:
		L.append(lines)
	return

'''
load_line_file(file_object)
Borrowed from rings.py, a script by Daniel Hoffman, professor at UVic, 2017.

Purpose:
	Takes an open file of line definitions, and puts them into a list of Line_Point.py
	line objects.

Preconditions:
	All line definitions use a cartesian coordinate system, with an origin at the middle
	of the canvas. The only whitespace characters are line breaks and spaces - no tabs.
'''
def load_line_file(file_object):
	line_objects = [ ]
	for line in file_object:
		# convert text line to a Line object
		line_object = line.split()
		point0 = Line_Point_colour.Point(float(line_object[1]), float(line_object[2]))
		point1 = Line_Point_colour.Point(float(line_object[3]), float(line_object[4]))
		line_object = Line_Point_colour.Line(point0, point1, line_object[5])

		line_objects.append(line_object)
	
	return line_objects

# Parse parameters
the_lines = open(sys.argv[1])
the_planes = str(sys.argv[2])
n = int(sys.argv[3])
line_object_list = load_line_file(the_lines)

# Perform mirror operation
if the_planes == 'x':
	mirror_x(line_object_list)
elif the_planes == 'y':
	mirror_y(line_object_list)
elif the_planes == 'xy':
	mirror_x(line_object_list)
	mirror_y(line_object_list)
elif the_planes == 'none':
	pass
else:
	sys.exit('Use: "file_name.txt planes n", where planes is "none", "x", "y", or "xy"')

# Perform rotation
for i in range(0, n):
	if i == 0:
		continue
	rads = i*math.pi*2/n
	rotate_copy(line_object_list, rads)

# Print results to stdout
print_lines(line_object_list)
