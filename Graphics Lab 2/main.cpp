#include <windows.h>
#include <GL/glut.h>
#include<stdio.h>
#include<conio.h>

float x1,x2,y1,y2, stepsize;
float xinc=0, yinc=0;

void init()
{
    glClearColor(0.0,1,0,0.0);
    glMatrixMode(GL_PROJECTION);
    gluOrtho2D(0.0,320,0.0,320);
}

void display() {
   glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
   glClear(GL_COLOR_BUFFER_BIT);


glBegin(GL_POINTS);
glColor3f(1.0f, 0.0f, 0.0f);


    float dx=x2-x1;
    float dy=y2-y1;


    if ( abs(dx)>  abs(dy))
        stepsize=abs(dx);
    else
        stepsize=abs(dy);

    float xinc=dx/stepsize;
    float yinc=dy/stepsize;

    float x=x1;
    float y=y1;

    glVertex2i(x,y);

    do{
        x=x+xinc;
        y=y+yinc;
        glVertex2i(x,y);
        stepsize--;
        printf("%f %f",x,y);
    } while(stepsize>0);
glEnd();

   glFlush();
}

int main(int argc, char** argv) {
     printf("Enter starting Point");
    scanf("%f %f",&x1,&y1);
    printf("Enter end point");
    scanf("%f %f",&x2,&y2);

   glutInit(&argc, argv);
   glutCreateWindow("OpenGL Setup Test");
   glutInitWindowSize(320, 320);
   glutInitWindowPosition(50, 50);
   init();
   glutDisplayFunc(display);
   glutMainLoop();
   return 0;
}
