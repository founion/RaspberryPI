#include <stdio.h>
#include <wiringPi.h>
#include <stdlib.h>

#define buzzer_pin 1  // buzzer는 18번에 연결
#define sw1 3         // sw1은 22번에 연결
#define sw2 4         // sw2은 23번에 연결
#define sw3 5         // sw3은 24번에 연결
#define sw4 6         // sw4은 25번에 연결

const int melody[] = {262, 294, 330, 349, 392, 440, 494, 523, 587};

void twinkle();
void foxrain();
void Jinglebell();
void stop_song();
void program_down();

int main(void){
	wiringPiSetup();

	pinMode(sw1, INPUT);
	pinMode(sw2, INPUT);
	pinMode(sw3, INPUT);
	pinMode(sw4, INPUT);

	pinMode(buzzer_pin, PWM_OUTPUT);

	pwmSetClock(19);
	pwmSetMode(PWM_MODE_MS);

	printf("SW1 : Twinkle\nSW2 : 여우비\nSW3 : Jinglebell\n");
	printf("SW4 : Exit\n");
	while(1) {
		if(digitalRead(sw1) == 0) twinkle();
		else if(digitalRead(sw2) == 0) foxrain();
		else if(digitalRead(sw3) == 0) Jinglebell();
		else if(digitalRead(sw4) == 0) program_down();
	}

	return 0;
}

void twinkle() {
	int twinkle[] = {1,1,5,5,6,6,5,4,4,3,3,2,2,1,
			 5,5,4,4,3,3,2,5,5,4,4,3,3,2,
			 1,1,5,5,6,6,5,4,4,3,3,2,2,1};
	printf("재생 중인 곡 : Twinkle\n");

	for(int i=0;i<sizeof(twinkle)/sizeof(twinkle[0]);i++) {
		if(digitalRead(sw2) == 0) {
			stop_song();
			foxrain();
			break;
		}
		else if(digitalRead(sw3) == 0) {
			stop_song();
			Jinglebell();
			break;
		}
		else if(digitalRead(sw4) == 0) {
			stop_song();
			program_down();
		}
		int index = twinkle[i];
		pwmSetRange(1000000/melody[index]);
		pwmWrite(buzzer_pin, 1000000/melody[index]/10);

		if(i==6 || i==13 || i==20 || i==27 || i==34 || i==41) delay(1000);
		else delay(500);
	}

	pwmWrite(buzzer_pin, 0);
}

void foxrain() {
	int foxrain[] = {3,2,3,2,
			 3,5,3,
			 3,2,3,2,
			 3,5,3,
			 3,2,3,4,5,
			 3,2,3,4,5,
			 3,2,3,4,5,7,5};
	printf("재생 중인 곡 : 여우비\n");

	for(int i=0;i<sizeof(foxrain)/sizeof(foxrain[0]);i++) {
		if(digitalRead(sw1) == 0) {
			stop_song();
			twinkle();
			break;
		}
		else if(digitalRead(sw3) == 0) {
			stop_song();
			Jinglebell();
			break;
		}
		else if(digitalRead(sw4) == 0) {
			stop_song();
			program_down();
		}
		int index = foxrain[i];
		pwmSetRange(1000000/melody[index]);
		pwmWrite(buzzer_pin, 1000000/melody[index]/10);

		if(i==3 || i==10) delay(400);
		else if(i==6 || i==13 || i==18 || i==23) delay(800);
		else delay(300);
	}

	pwmWrite(buzzer_pin, 0);
}

void Jinglebell() {
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
	printf("재생 중인 곡 : Jinglebell\n");

	for(int i=0;i<sizeof(bell)/sizeof(bell[0]);i++) {
		if(digitalRead(sw1) == 0) {
			stop_song();
			twinkle();
			break;
		}
		else if(digitalRead(sw2) == 0) {
			stop_song();
			foxrain();
			break;
		}
		else if(digitalRead(sw4) == 0) {
			stop_song();
			program_down();
		}
		int index = bell[i];
		pwmSetRange(1000000/melody[index]);
		pwmWrite(buzzer_pin, 1000000/melody[index]/10);

		if(i==4 || i==9 || i==14 || i==20 || i==25 || i==30 || i==43 || i==54 || i==68 || i==79) delay(1000);
		else delay(500);
	}

	pwmWrite(buzzer_pin, 0);
}

void stop_song() {
	pwmWrite(buzzer_pin, 0);
}

void program_down() {
	printf("프로그램을 종료합니다\n");
	exit(0);
}
