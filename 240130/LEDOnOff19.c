#include <stdio.h>
#include <wiringPi.h>

#define led_pin 21

int main(void){
	wiringPiSetup();

	pinMode(led_pin, OUTPUT);

	while(1) {
			digitalWrite(led_pin, HIGH);
			delay(1);
			digitalWrite(led_pin, LOW);
			delay(9);
	}
}
