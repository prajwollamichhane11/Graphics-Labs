from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
from math import *

points = [[20, 20, 10], [20, 40, 30], [40, 40, 10]]
print('Select \n1. Translate \n2. Rotate \n3. Scale')
select = int(input('Enter your selection: '))


def matrixMultiply(A, B):
    prod = list()
    for i in range(4):
        sm = 0
        for j in range(4):
            sm += A[i][j] * B[j][0]
        prod.append(sm)
    return prod


def translate():
    translated = list()
    translate_mat = [[1, 0, 0, tx],
                     [0, 1, 0, ty],
                     [0, 0, 1, tz],
                     [0, 0, 0, 1]]
    for point in points:
        point_mat = [[point[0]], [point[1]], [point[2]], [1]]
        translated.append(matrixMultiply(translate_mat, point_mat))
    points.extend(translated)

def scale():
    translated = list()
    scale_mat = [[sx, 0, 0, 0],
                 [0, sy, 0, 0],
                 [0, 0, sz, 0],
                 [0, 0, 0, 1]]
    for point in points:
        point_mat = [[point[0]], [point[1]], [point[2]], [1]]
        translated.append(matrixMultiply(scale_mat, point_mat))
    points.extend(translated)



def rotate():
    translated = list()
    if axs == 1:
        rotate_mat = [[1, 0, 0, 0],
                      [0, cos(theta), -sin(theta), 0],
                      [0, sin(theta), cos(theta), 0],
                      [0, 0, 0, 1]]
    elif axs == 2:
        rotate_mat = [[cos(theta), 0, sin(theta), 0],
                      [0, 1, 0, 0],
                      [-sin(theta), 0, cos(theta), 0],
                      [0, 0, 0, 1]]
    elif axs == 3:
        rotate_mat = [[cos(theta), -sin(theta), 0, 0],
                      [sin(theta), cos(theta), 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]]
    for point in points:
        point_mat = [[point[0]], [point[1]], [point[2]], [1]]
        translated.append(matrixMultiply(rotate_mat, point_mat))
    points.extend(translated)


if select == 1:
    tx = int(input('Enter tx: '))
    ty = int(input('Enter ty: '))
    tz = int(input('Enter tz: '))
    translate()
elif select == 2:
    theta = int(input('Enter angle of rotation: '))
    print('1. X-axis\n2. Y-axis \n3. Z-axis \n')
    axs = int(input('Select Axis: '))
    rotate()
elif select == 3:
    sx = int(input('Enter sx: '))
    sy = int(input('Enter sy: '))
    sz = int(input('Enter sz: '))
    scale()

def drawAxes():
    glBegin(GL_LINES)
    glVertex3i(1, 0, 0)
    glVertex3i(-1, 0, 0)
    glVertex3i(0, 1, 0)
    glVertex3i(0, -1, 0)
    glVertex3i(0, 0, 1)
    glVertex3i(0, 0, -1)
    glEnd()

def calcDiv():
    div = 0
    for point in points:
        div = max(div, point[0], point[1], point[2])
    return div * 1.05

def drawPolygon():
    drawAxes()
    div = calcDiv()
    count = 0
    glBegin(GL_TRIANGLES)
    for point in points:
        glVertex3f(point[0] / div, point[1] / div, point[2] / div)
        count += 1
    glEnd()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(350, 150)
    glutCreateWindow(b'3D Transformations')
    glutDisplayFunc(drawPolygon)
    glutMainLoop()


if __name__ == '__main__':
    main()

