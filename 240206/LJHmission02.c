#include <stdio.h>
#include <wiringPi.h>

#define buzzer_pin 1  // buzzer는 18번에 연결

const int melody[] = {262, 294, 330, 349, 392, 440, 494, 523, 587};

int bell[] = {0,5,4,3,0,
	    0,5,4,3,1,
	    0,6,5,4,2,
	    7,7,6,4,5,3,
	    0,5,4,3,0,
	    0,5,4,3,1,
	    1,6,5,4,7,7,7,7,8,7,6,4,3,
	    5,5,5,5,5,5,5,7,3,4,5,
	    6,6,6,6,6,5,5,5,5,4,4,3,4,7,
	    5,5,5,5,5,5,5,7,3,4,5,
	    6,6,6,6,6,5,4,4,7,7,6,4,3};

int main(void){
	int i;

	wiringPiSetup();
	pinMode(buzzer_pin, PWM_OUTPUT);

	pwmSetClock(19);
	pwmSetMode(PWM_MODE_MS);

	for(i=0;i<sizeof(bell)/sizeof(bell[0]);i++) {
		int index = bell[i];
		pwmSetRange(1000000/melody[index]);
		pwmWrite(buzzer_pin, 1000000/melody[index]/10);

		if(i==4 || i==9 || i==14 || i==20 || i==25 || i==30 || i==43 || i==54 || i==68 || i==79) delay(1000);
		else delay(500);
	}

	pwmWrite(buzzer_pin, 0);
	return 0;
}
