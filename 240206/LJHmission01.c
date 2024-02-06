#include <stdio.h>
#include <wiringPi.h>

#define red_pin 15   // red는 14에 연결
#define green_pin 16 // green은 15에 연결
#define blue_pin 1   // blue는 18에 연결

int main(){
	int i;

	wiringPiSetup();

	pinMode(red_pin, OUTPUT);
	pinMode(green_pin, OUTPUT);
	pinMode(blue_pin, OUTPUT);

	digitalWrite(red_pin, LOW);
	digitalWrite(green_pin, LOW);
	digitalWrite(blue_pin, LOW);

	printf("3 Color LED Control Start !!\n");

	for(i=0;i<10;i++) {
		printf("Red LED On!!\n");
		digitalWrite(red_pin, HIGH);
		delay(500);
		printf("Red LED Off!!\nGreen LED On!!\n");
		digitalWrite(red_pin, LOW);
		digitalWrite(green_pin, HIGH);
		delay(500);
		printf("Green LED Off!!\nBlue LED On!!\n");
		digitalWrite(green_pin, LOW);
		digitalWrite(blue_pin, HIGH);
		delay(500);
		printf("Blue LED Off\n");
		digitalWrite(blue_pin, LOW);
	}

	return 0;
}
