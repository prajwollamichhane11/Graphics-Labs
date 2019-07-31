from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

print('For start point: ')
x1 = float(input('Enter x: '))
y1 = float(input('Enter y: '))
print('For end point: ')
x2 = float(input('Enter x: '))
y2 = float(input('Enter y: '))
x_min = float(input('Enter x_min: '))
y_min = float(input('Enter y_min: '))
x_max = float(input('Enter x_max: '))
y_max = float(input('Enter y_max: '))

point_array = [[x1, y1], [x2, y2]]


def drawAxes():
    glColor(0, 0, 1, 0)
    glBegin(GL_LINES)
    glVertex2i(1, 0)
    glVertex2i(-1, 0)
    glVertex2i(0, 1)
    glVertex2i(0, -1)
    glEnd()
    glColor(1, 1, 1, 1)

def drawClippingWindow(div):
    glBegin(GL_LINE_LOOP)
    glVertex2f(x_min / div, y_min / div)
    glVertex2f(x_max / div, y_min / div)
    glVertex2f(x_max / div, y_max / div)
    glVertex2f(x_min / div, y_max / div)
    glEnd()

def calcDiv(points):
	div = max(abs(x_min), abs(x_max), abs(y_min), abs(y_max))
	for i in points:
		for j in i:
			div = max(div, abs(j))

	return div + 1


def calcRegionCode(point):
	r_code = list()
	if point[0] < x_min:
		r_code.extend([1, 0])
	elif point[0] > x_max:
		r_code.extend([0, 1])
	else:
		r_code.extend([0, 0])

	if point[1] < y_min:
		r_code.extend([1, 0])
	elif point[1] > y_max:
		r_code.extend([0, 1])
	else:
		r_code.extend([0, 0])

	return r_code


def clip(r_code, points, m):
	clipped = list()
	if r_code[0] == 1:
		clipped = leftClipper(points, m)
	if r_code[1] == 1:
		clipped = rightClipper(points, m)
	if r_code[2] == 1:
		clipped = bottomClipper(points, m)
	if r_code[3] == 1:
		clipped = topClipper(points, m)
	return clipped


def leftClipper(points, m):
	x = x_min
	y = points[1][1] - m * (points[1][0] - x)
	return [x, y]


def rightClipper(points, m):
	x = x_max
	y = points[1][1] - m * (points[1][0] - x)
	return [x, y]


def bottomClipper(points, m):
	y = y_min
	x = (m * points[1][0] - (points[1][1] - y)) / m
	return [x, y]


def topClipper(points, m):
	y = y_max
	x = (m * points[1][0] - (points[1][1] - y)) / m
	return [x, y]


def AND(r_code1, r_code2):
	anded = ''
	for i, j in zip(r_code1, r_code2):
		anded += str(i * j)
	return anded

def drawPoints(points, div, color='r'):
	if color == 'g':
		glColor(0, 1, 0, 0)
	elif color == 'r':
		glColor(1, 0, 0, 0)
	glBegin(GL_LINES)
	for i in points:
		glVertex2f(i[0] / div, i[1] / div)
	glEnd()

def cohenSutherland():
	drawAxes()
	points = point_array
	div = calcDiv(points)
	drawClippingWindow(div)
	drawPoints(points, div)
	if points[0][0] != points[1][0]:
		m = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0])
	else:
		m = float('inf')

	r_code1 = calcRegionCode(points[0])
	r_code2 = calcRegionCode(points[1])
	if AND(r_code1, r_code2) == '0000':
		if r_code1 == [0, 0, 0, 0] and r_code2 == [0, 0, 0, 0]:
			print('Line lies completely inside the clipping window.')
			drawPoints(points, div, color='g')

		elif r_code2 == [0, 0, 0, 0]:
			points[0] = clip(r_code1, points)
			print('Intersection point is ({}, {}).'.format(points[0][0], points[0][1]))
			drawPoints(points, div, color='g')

		elif r_code1 == [0, 0, 0, 0]:
			points[1] = clip(r_code2, points, m)
			print('Intersection point is ({}, {}).'.format(points[1][0], points[1][1]))
			drawPoints(points, div, color='g')

		else:
			points[0] = clip(r_code1, points, m)
			r_code1 = calcRegionCode(points[0])
			if AND(r_code1, r_code2) == '0000':
				points[1] = clip(r_code2, points, m)
				r_code2 = calcRegionCode(points[1])
				print('Intersection points are ({}, {}) and ({}, {}).'.format(points[0][0], points[0][1], points[1][0], points[1][1]))
				drawPoints(points, div, color='g')
			else:
				print('Line lies completely outside the clipping window.')

	else:
		print('Line lies completely outside the clipping window.')

	glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(350, 150)
    glutCreateWindow(b'Line Clipping')
    glutDisplayFunc(cohenSutherland)
    glutMainLoop()

if __name__ == '__main__':
	main()
