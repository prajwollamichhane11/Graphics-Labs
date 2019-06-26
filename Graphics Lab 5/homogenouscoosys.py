from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import sin, cos, radians, pi
import sys


def translation(x,y,tx,ty):

	T= [[1, 0, tx],[0, 1, ty],[0, 0, 1]]

	P =[[x],[y],[1]]

	result= [[0],
	  	 [0],
	   	 [0]]

    #Matrix multiplication result=T.P
	# iterate through rows of T
	for i in range(len(T)):
		# iterate through columns of P
		for j in range(len(P[0])):
			# iterate through rows of P
			for k in range(len(P)):
				result[i][j] += T[i][k] * P[k][j]

	return result[0][0],result[1][0]

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
       
    print("Enter the first point of triangle")
    x1,y1=map(float,input().split())
    print("Enter the second point of triangle")
    x2,y2=map(float,input().split())
    print("Enter the third point of triangle")
    x3,y3=map(float,input().split())
    
    print("Enter translation factor tx and ty")
    tx,ty=map(int,input().split())


    glBegin(GL_TRIANGLES)
    glColor(1.0, 0.0, 0.0)
    glVertex3f(x1/300,y1/300,0.0)
    glVertex3f(x2/300,y2/300,0.0)
    glVertex3f(x3/300,x3/300,0.0)
    glEnd()
    
    x1t,y1t=translation(x1,y1,tx,ty)
    x2t,y2t=translation(x2,y2,tx,ty)
    x3t,y3t=translation(x3,y3,tx,ty)
    
    print(x2,y2)
    print(x2t,y2t)

    glBegin(GL_TRIANGLES)
    glColor(0.0, 1.0, 0.0)
    glVertex3f(x1t/300,y1t/300,0.0)
    glVertex3f(x2t/300,y2t/300,0.0)
    glVertex3f(x3t/300,x3t/300,0.0)
    glEnd()
    
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_ALPHA|GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Transformation")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(draw)
    glutMainLoop()

main()
