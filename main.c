
/*Designed by Shubhojyoti Ganguly
	Team NARM
	
	ADVANCED LINE FOLLOWER WITH PID CONTROL
*/

#define F_CPU 12000000UL

#include<avr/io.h>
#include<util/delay.h>

#define MAX_SPEED 1023
#define MIN_SPEED 0

#define ROBOT_SPEED 200

#define SENSOR_THRESH 800
#define DELAY 1

#define SCALE (MAX_SPEED/ROBOT_SPEED)

float Kp = 100;	//Proportional Gain
float Ki =  0.01;	//Integral Gain
float Kd =  90;	//Differential Gain


int32_t eInteg = 0;	//Integral accumulator
int32_t ePrev  =0;		//Previous Error


#define M_CW 1
#define M_CCW 2
#define M_STOP 0


//--------------------------------------------------------------------
//Motor Control Functions

void MotorInit()
{
	DDRD|=(1<<PD4)|(1<<PD5)|(1<<PD6)|(1<<PD7);//Motor direction control pins to output
	DDRB|=(1<<PB1)|(1<<PB2);//Motor PWM pins to output
	TCCR1A|=(1<<COM1A1)|(1<<COM1B1)|(1<<WGM11)|(1<<WGM10);//Phase Correct WGM without using interrupt
    
	TCCR1B|=(1<<CS11)|(1<<CS10);//Prescaler 64
}

void MotorA(uint8_t dir,uint8_t speed)
{
	
	if(dir==M_CW)
	{
		PORTD&=~(1<<PD4);
		PORTD|=(1<<PD5);
		
	}
	if(dir==M_CCW)
	{
		PORTD&=~(1<<PD5);
		PORTD|=(1<<PD4);
		
	}
	if(dir==M_STOP)
	{
		PORTD&=~(1<<PD4);
		PORTD&=~(1<<PD5);
		
	}

	OCR1A=SCALE*speed;
	TCNT1=0;

}



void MotorB(uint8_t dir,uint8_t speed)
{
	
	if(dir==M_CW)
	{
		PORTD&=~(1<<PD6);
		PORTD|=(1<<PD7);
		
	}
	if(dir==M_CCW)
	{
		PORTD&=~(1<<PD6);
		PORTD|=(1<<PD7);
		
	}
	if(dir==M_STOP)
	{
		PORTD&=~(1<<PD6);
		PORTD&=~(1<<PD7);
		
	}
	OCR1B=SCALE*speed;
	TCNT1=0;

}

//End of motor control fuctions

//-------------------------------------------------------------------------------

//ADC related functions

int ADCsingleREAD(uint8_t adctouse)
{
    int ADCval;

    ADMUX = adctouse;         // use #1 ADC
    ADMUX |= (1 << REFS0)|(1<<REFS1);    // use AVcc as the reference
    ADMUX &= ~(1 << ADLAR);   // clear for 10 bit resolution
    
    ADCSRA |= (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);    // 128 prescale for 8Mhz
    ADCSRA |= (1 << ADEN);    // Enable the ADC

    ADCSRA |= (1 << ADSC);    // Start the ADC conversion

    while(ADCSRA & (1 << ADSC));      // Thanks T, this line waits for the ADC to finish 


    ADCval = ADCL;
    ADCval = (ADCH << 8) + ADCval;    // ADCH is read so ADC can be updated again

    return ADCval;
}
int readSensors()//returns a number from 0 to 5 which gives the position of black line
{
	int sensor1,sensor2,sensor3,sensor4,sensor5;
	float avgSensor;
	sensor1=ADCsingleREAD(5);
	ADCSRA=0X00;
	ADMUX=0x00;
	ADCL=0;
	sensor2=ADCsingleREAD(4);
	ADCSRA=0X00;
	ADMUX=0x00;
	ADCL=0;
	sensor3=ADCsingleREAD(3);
	ADCSRA=0X00;
	ADMUX=0x00;
	ADCL=0;
	sensor4=ADCsingleREAD(2);
	ADCSRA=0X00;
	ADMUX=0x00;
	ADCL=0;
	sensor5=ADCsingleREAD(1);
	ADCSRA=0X00;
	ADMUX=0x00;
	ADCL=0;
	if(sensor1>SENSOR_THRESH)
	sensor1=1;
	else
	sensor1=0;
	if(sensor2>SENSOR_THRESH)
	sensor2=1;
	else
	sensor2=0;
	if(sensor3>SENSOR_THRESH)
	sensor3=1;
	else
	sensor3=0;
	if(sensor4>SENSOR_THRESH)
	sensor4=1;
	else
	sensor4=0;
	if(sensor5>SENSOR_THRESH)
	sensor5=1;
	else
	sensor5=0;
	if(sensor1==0 && sensor2==0 && sensor3==0 && sensor4==0 && sensor5==0)
	{
		return 0xFF;
	}		
   
	// Calculate weighted mean
	avgSensor = (float) sensor1*1 + sensor2*2 + sensor3*3 + sensor4*4 + sensor5*5 ;
	avgSensor = (float) avgSensor / (sensor1 + sensor2 + sensor3 + sensor4 + sensor5);

	return avgSensor;
	


}

//End of ADC related functions

//--------------------------------------------------------------------

//PID Control

float PID(float cur_value,float req_value)
{
  float pid;
  float error;

  error = req_value - cur_value;         
  pid = (Kp * error)  + (Ki * eInteg) + (Kd * (error - ePrev)/DELAY); 

  eInteg += error*DELAY;            // integral is simply a summation over time
  ePrev = error;                    // save previous for derivative

  return pid;
}


//---------------------------------------------------------------
//Line Follower control
void control(float control)
{
	if(control > 2*ROBOT_SPEED)
		control=2*ROBOT_SPEED;
	if(control < -2*ROBOT_SPEED)
		control=-2*ROBOT_SPEED;
	if(control>0.0)
	{
		if(control<ROBOT_SPEED)
		{
			MotorA(M_CCW,ROBOT_SPEED);
			MotorB(M_CCW,ROBOT_SPEED-control);
		
			//Needs to turn medium right 
		}
	
		else
		{
			MotorA(M_CCW,ROBOT_SPEED);
			MotorB(M_CW,control-ROBOT_SPEED);
				
				//Need to turn sharp right
		}
	}
	if(control<0.0)
	{
		if(control>-255)
		{
			MotorB(M_CCW,ROBOT_SPEED);
			MotorA(M_CCW,ROBOT_SPEED+control);
			//Need to turn medium left
		}
		else
		{
			MotorA(M_CW,-control-ROBOT_SPEED);
			MotorB(M_CCW,ROBOT_SPEED);
			
			//Need to turn sharp left
		}
	}
}






//End of all controls

//------------------------------------------------------------
//------------------------------------------------------------

//Main function for line follower
int main()
{
	
	//float s=0.0f,control=0.0f;
	MotorInit();
	while(1)
	{
		control(PID(readSensors(),3.0));		
		_delay_ms(DELAY);
		
	
	}		
		
	return -1;
}
