#include<windows.h>
#ifdef _APPLE_
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

#include <stdlib.h>

#include <stdlib.h>
#include<iostream>

using namespace std;

int x[100];
int length;

void displayAxes(){
    glClear(GL_COLOR_BUFFER_BIT);
    for(int i=-300;i<=300;i++){
        glBegin(GL_POINTS);
        glColor3f(1.0f, 0.0f, 0.0f);
        glVertex2f(0,i/300.0);
        glEnd();
        glBegin(GL_POINTS);
        glVertex2f(i/300.0,0);
        glEnd();
    }
 }

void display(){
    displayAxes();
    int x1,x2,y1,y2,xinc,yinc,dx,dy,P;
    int a,b;
    glBegin(GL_POINTS);

    int fx1= 0;
    int fx2= 20;
    for(int j=0;j<length;j++){
        fx1=fx2;
        fx2+=280/length;
        while(fx1<fx2){
//x coordinate not fixed
            x1=fx1;
            x2=fx1;
            y1=x[j];
            y2=0;
            dx = x2-x1;
            dy = y2-y1;

            if(abs(dy)<abs(dx)){//m<1
                a=dy;
                b=dx;
            }
            else{
                a=dx;
                b=dy;
            }
            xinc=1;
            yinc=1;
            if(dy<0){
                yinc=-1;
            }
            if(dy==0){
                yinc=0;
            }

            if(dx<0){
                xinc=-1;
            }
            if(dx==0){
                xinc=0;
            }
            P = 2*a-b;
            glBegin(GL_LINES);
            glColor3f(0.0f, 1.0f, 0.0f);
            glVertex2f(x1/300.0,y1/300.0);
            for(int i=0;i<abs(b);i++){
                cout<<x1<<","<<fx1<<endl;
                if(P<0){
                    if(abs(dy)>abs(dx)){
                        y1+=yinc;
                    }
                    else{
                    x1+=xinc;
                    }
                    P=P+2*a;

                }
                else{
                    P=P+2*a-2*b;
                    x1+=xinc;
                    y1+=yinc;
                }

                glBegin(GL_POINTS);
                glColor3f(0.0f, 0.0f, 1.0f);
                glVertex2f(x1/300.0,y1/300.0);
            }
            glBegin(GL_POINTS);
            glColor3f(0.0f, 1.0f, 0.0f);
            glVertex2f(x1/300.0,y1/300.0);
            fx1+=4;
        }
    }

    glEnd();
    glFlush();
}
int main(int argc, char *argv[])
{
    cout<<"Input the no. of items in Histogram"<<endl;
    cin>>length;
    for (int i=0;i<length;i++){
        cout<<"Frequency "<<i<<":";
        cin>>x[i];
        cout<<"Next point"<<endl;
    }

    glutInit(&argc, argv);
    glutInitWindowSize(600,600);
    glutInitWindowPosition(0,0);
    glutInitDisplayMode(GLUT_SINGLE);
    glutCreateWindow("Prajwol- Lab 3");
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}


