//import the neccesary mdoule to control GPIOs
#include <wiringPi.h>
#include <stdio.h>
#include <unistd.h>
#include <termios.h>
#include <fcntl.h>

int getch(void)
{
    int ch;
    struct termios oldt, newt;
    long oldf, newf;

    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;
    newt.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    oldf = fcntl(STDIN_FILENO, F_GETFL, 0);
    newf = oldf | O_NONBLOCK;
    fcntl(STDIN_FILENO, F_SETFL, newf);
    ch = getchar();
    fcntl(STDIN_FILENO, F_SETFL, oldf);
    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
    return ch;
}

//make global variables to store the wiring pi pin numbers for the motors
int m1a = 0;
int m1b = 1;
int m2a = 3;
int m2b = 4;

//make robot go forwards
void forwards()
{
  digitalWrite(m1a, HIGH);
  digitalWrite(m1b, LOW);
  digitalWrite(m2a, HIGH);
  digitalWrite(m2b, LOW);
}

//all motors off
void stop()
{
  digitalWrite(m1a, LOW);
  digitalWrite(m1b, LOW);
  digitalWrite(m2a, LOW);
  digitalWrite(m2b, LOW);
}

//Make both motors turn backwards
void reverse()
{
  digitalWrite(m1a, LOW);
  digitalWrite(m1b, HIGH);
  digitalWrite(m2a, LOW);
  digitalWrite(m2b, HIGH);
}

//Make motors turn fwd, bak
void left()
{
  digitalWrite(m1a, HIGH);
  digitalWrite(m1a, LOW);
  digitalWrite(m1a, LOW);
  digitalWrite(m1a, HIGH);
}

//Make motors turn fwd, bak
void right()
{
  digitalWrite(m1a, LOW);
  digitalWrite(m1a, HIGH);
  digitalWrite(m1a, HIGH);
  digitalWrite(m1a, LOW);
}

//main function
int main(void)
{
    int x;
    do {
       usleep(500000000);
       if ((x = getch()) != EOF) {
         switch(x) {
          case 'W':
          case 'w':
            forwards();
            printf("W was pressed \n");
            break;
          case 'A':
          case 'a':
            left();
            printf("A was pressed \n");
            break;
          case 's':
          case 'S':
            reverse();
            printf("S was pressed \n");
            break;
          case 'D':
          case 'd':
            right();
            printf("D was pressed \n");
            break;
        }
       } else {
          printf("stop");
          stop();
       }
    } while (x != 'q');
    return 0;
}
