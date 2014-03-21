#include<avr/io.h>
#include<util/delay.h>

#define MAX_SPEED 1023
#define MIN_SPEED 0

#define ROBOT_SPEED 200

#define SCALE (MAX_SPEED/ROBOT_SPEED)

#define M_CW 1
#define M_CCW 2
#define M_STOP 0


void MotorA(uint8_t speed,uint8_t dir)
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



void MotorB(uint8_t speed,uint8_t dir)
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


void main()
{
	DDRB|=(1<<PB1)|(1<<PB2);
	DDRD|=(1<<PD7)|(1<<PD5)|(1<<PD4)|(1<<PD6);
	
	
	TCCR1A|=(1<<COM1A1)|(1<<COM1B1)|(1<<WGM11)|(1<<WGM10);	
    
	TCCR1B|=(1<<CS11)|(1<<CS10);
	OCR1B=SCALE*200;
	
	while(1)
	{
		MotorA(10,M_CCW);
		MotorB(200,M_CW);
		_delay_ms(5000);
		//Forward
		MotorA(80,M_CCW);
		MotorB(200,M_CW);
		
		_delay_ms(5000);
		//Left
		MotorA(150,M_CCW);
		MotorA(200,M_CW);
		_delay_ms(5000);
		
		
		
		
		
	}
}