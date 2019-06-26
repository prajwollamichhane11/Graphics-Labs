//Ellipse Drawing by midpoint approach
#include <windows.h>
#include <GL/glut.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

float xc = 0, yc = 0, rx = 200 , ry = 100;

void DisplayAxes(){
    glColor3f(255,255 ,255);
    glBegin(GL_LINES);
        glVertex2f(0,1);
        glVertex2f(0,-1);
        glVertex2f(-1,0);
        glVertex2f(1,0);
    glEnd();
}
midPointEllipse(float xc, float yc, float rx, float ry){
    float x = 0, y = ry;
    float dx, dy, d1, d2;
    dx = 2 * ry * ry * x;
    dy = 2 * rx * rx * y;
    d1 = (ry * ry)-(rx * rx * ry)+(0.25 * rx * rx);
    d2 = ((ry * ry) * ((x + 0.5) * (x + 0.5))) + ((rx * rx) * ((y - 1) * (y - 1))) - (rx * rx * ry * ry);

    //for region 1
    while(dx < dy){
        glVertex2f((x+xc)/500, (y+yc)/500);
        glVertex2f((-x+xc)/500, (y+yc)/500);
        glVertex2f((x+xc)/500, (-y+yc)/500);
        glVertex2f((-x+xc)/500, (-y+yc)/500);

        if(d1 < 0){
            x++;
            dx = dx + (2*ry*ry);
            d1 = d1 + dx+ (ry*ry);
        }
        else{
            x++;
            y--;
            dx = dx + (2*ry*ry);
            dy = dy - (2*rx*rx);
            d1 = d1 + dx - dy +(ry*ry);
        }
    }
    while(dx>dy && y>=0){

        glVertex2f((x+xc)/500, (y+yc)/500);
        glVertex2f((-x+xc)/500, (y+yc)/500);
        glVertex2f((x+xc)/500, (-y+yc)/500);
        glVertex2f((-x+xc)/500, (-y+yc)/500);

        if(d2 > 0){
            y--;
            dy = dy - (2*rx*rx);
            d2 = d2 + (rx*rx) - dy;
        }
        else{
            y--;
            x++;
            dx = dx + (2*ry*ry);
            dy = dy - (2*rx*rx);
            d2 = d2 + dx -dy + (rx*rx);
        }
    }

}
void DisplayLine()
{
	glClear (GL_COLOR_BUFFER_BIT);
	DisplayAxes();
	glColor3ub(255, 80, 0);

    glBegin(GL_POINTS);
	midPointEllipse(xc, yc, rx, ry);

    glEnd();
	glFlush ();
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode (GLUT_SINGLE);
	glutInitWindowSize (1000, 1000);
	glutInitWindowPosition (100, 100);
	glutCreateWindow ("Ellipse Drawing Algorithm");
	glutDisplayFunc(DisplayLine);

	glutMainLoop();
    return 0;
}
