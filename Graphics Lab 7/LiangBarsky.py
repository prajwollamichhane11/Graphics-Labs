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

points = [[x1, y1], [x2, y2]]

dx = points[1][0] - points[0][0]
dy = points[1][1] - points[0][1]



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


def calcDiv():
	div = max(abs(x_min), abs(x_max), abs(y_min), abs(y_max))
	for i in points:
		for j in i:
			div = max(div, abs(j))
	return div + 1


def drawPoints(points, div, color='r'):
	if color == 'g':
		glColor(0, 1, 0, 0)
	elif color == 'r':
		glColor(1, 0, 0, 0)
	glBegin(GL_LINES)
	for i in points:
		glVertex2f(i[0] / div, i[1] / div)
	glEnd()


def liangBarsky():
	drawAxes()
	div = calcDiv()
	drawClippingWindow(div)
	drawPoints(points, div)
	p = [-dx, dx, -dy, dy]
	q = [points[0][0] - x_min,
	     x_max - points[0][0],
	     points[0][1] - y_min,
	     y_max - points[0][1]]
	u1 = 0
	u2 = 1

	for i in range(4):
		if p[i] != 0:
			r = (q[i] / p[i])
		else:
			r = float('inf')

		if p[i] < 0:
			u1 = max(u1, r)
		else:
			u2 = min(u2, r)

	if u1 > u2:
		print('Line lies completely outside clipping window.')
	else:
		x1 = points[0][0] + u1 * dx
		y1 = points[0][1] + u1 * dy
		x2 = points[0][0] + u2 * dx
		y2 = points[0][1] + u2 * dy
		line = [[x1, y1], [x2, y2]]
		drawPoints(line, div, color='g')
		print('End points of line in the clipping window are ({}, {}) and ({}, {}).'.format(x1, y1, x2, y2))

	glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(350, 150)
    glutCreateWindow(b'Line Clipping')
    # gluOrtho2D(-50, 50, -50, 50)
    glutDisplayFunc(liangBarsky)
    glutMainLoop()


if __name__ == '__main__':
	main()

