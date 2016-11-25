#include <AFMotor.h>
#include <Servo.h>

Servo myservo;
AF_Stepper motor(200, 2);

void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);  
  motor.setSpeed(10);
  myservo.attach(22);
  myservo.write(45);
}

char c;

void Rotate(int d=90)
{
  uint8_t dir=FORWARD;
  uint16_t n=12;
  delay(1000);
  
  if(d==-90)
    dir = BACKWARD;
    
  else if(d==180)
    n=24;

  delay(2000);
  motor.step(n, dir, SINGLE);
  delay(2000);
}

void Push(int n=1)
{
    myservo.write(45);
    delay(2000);
    while(n--)
    {
      myservo.write(120);
      delay(2000);
      myservo.write(45);
      delay(2000);
    }
}

void Hold_Rotate(int d=90)
{
    myservo.write(45);
    delay(2000);
    myservo.write(100);
    delay(3000);
    Rotate(d); 
    delay(1000); 
    myservo.write(45);
    delay(2000);
}
void loop()
{
  
  if( Serial.available() > 0 )
	c = (char)Serial.read();
  
  if (c == 'L')
  {
    Rotate(-90);	//1.Rotate -90
    Push();			//2.Push
    Hold_Rotate();	//3.Hold and Rotate 90
    Push(3);		//4.Push X 3
    Rotate();		//5.Rotate +90
  }
  else if(c=='l')
  {
    Rotate(-90); 
    Push();
    Hold_Rotate(-90);
    Push(3);
    Rotate();
  }
  else if(c=='R')
  {
    Rotate();
    Push();
    Hold_Rotate();
    Push(3);
    Rotate(-90);
  }
  else if(c=='r')
  {
    Rotate();
    Push();
    Hold_Rotate(-90);
    Push(3);
    Rotate(-90); 
   }
  else if(c=='D')
  {
    Hold_Rotate(); 
  }
  else if(c=='d')
  {
    Hold_Rotate(-90);
  }
  else if(c=='U')
  {
    Push(2);
    Hold_Rotate();
    Push(2);
  }
  else if(c=='u')
  {
    Push(2);
    Hold_Rotate(-90);
    Push(2);    
  }
  else if(c=='F')
  {
    Push(3);
    Hold_Rotate();
    Push();
  }
  else if(c=='f')
  {
    Push(3);
    Hold_Rotate(-90);
    Push(1);
  }
  else if(c=='B')
  {
    Push();
    Hold_Rotate();
    Push(3);
    
  }
  else if(c=='b')
  {
    Push();
    Hold_Rotate(-90);
    Push(3);    
  }

  else if(c=='1')
  {
    //R2
    Rotate();
    Push();
    Hold_Rotate(180);
    Push(3);
    Rotate(-90); 
  }

  else if(c=='2')
  {
    //L2
    Rotate(-90);
    Push();
    Hold_Rotate(180);
    Push(3);
    Rotate();
  }
  else if(c=='3')
  {
    //B2
    Push();
    Hold_Rotate(180);
    Push(3);
  }
  else if(c=='4')
  {
    //F2
    Push(3);
    Hold_Rotate(180);
    Push();
  }
  else if(c=='5')
  {
    //U2
    Push(2);
    Hold_Rotate(180);
    Push(2);

  }
  else if(c=='6')
  {
	//D2
    Hold_Rotate(180);
  }
    
  c='#';

 }
