//Circle Drawing by midpoint approach
#include <windows.h>
#include <GL/glut.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

float pntx1=0, pnty1=0, r=100;

void DisplayAxes(){
    glColor3f(255,255,255);
    glBegin(GL_LINES);
        glVertex2f(0,1);
        glVertex2f(0,-1);
        glVertex2f(-1,0);
        glVertex2f(1,0);
    glEnd();
}

void midPointCircleAlgo(float pntx1, float pnty1, float r)
{
	float x = 0;
	float y = r;
	float decision = 5/4 - r;

    glVertex2f((x+pntx1)/300, (y+pnty1)/300);
	while (y > x)
	{
		if (decision < 0)
		{
			x++;
			decision += 2*x+1;
		}
		else
		{
			y--;
			x++;
			decision += 2*(x-y)+1;
		}
		glVertex2f((x+pntx1)/300, (y+pnty1)/300);
		glVertex2f((x+pntx1)/300, (-y+pnty1)/300);
		glVertex2f((-x+pntx1)/300, (y+pnty1)/300);
		glVertex2f((-x+pntx1)/300, (-y+pnty1)/300);
		glVertex2f((y+pntx1)/300, (x+pnty1)/300);
		glVertex2f((-y+pntx1)/300, (x+pnty1)/300);
        glVertex2f((y+pntx1)/300, (-x+pnty1)/300);
		glVertex2f((-y+pntx1)/300, (-x+pnty1)/300);
	}

}

void DisplayLine()
{
	glClear (GL_COLOR_BUFFER_BIT);
	DisplayAxes();
	glColor3ub(255, 80, 0);

    glBegin(GL_POINTS);
	midPointCircleAlgo(pntx1, pnty1, r);

    glEnd();
	glFlush ();
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode (GLUT_SINGLE);
	glutInitWindowSize (600, 600);
	glutInitWindowPosition (100, 100);
	glutCreateWindow ("Circle Drawing Algorithm");
	glutDisplayFunc(DisplayLine);

	glutMainLoop();
    return 0;
}
