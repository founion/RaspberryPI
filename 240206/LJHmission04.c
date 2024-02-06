#include <stdio.h>
#include <wiringPi.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#define sw1 3          // sw1는 22번에 연결
#define sw2 4          // sw2는 23번에 연결
#define sw3 5          // sw3는 24번에 연결
#define sw4 6          // sw4는 25번에 연결
#define STEP_OUTA 27   // STEP_OUTA는 16번에 연결
#define STEP_OUTB 0    // STEP_OUTB는 17번에 연결
#define STEP_OUT2A 1   // STEP_OUT2A는 18번에 연결
#define STEP_OUT2B 24  // STEP_OUT2B는 19번에 연결

void degree45();
void degree90();
void degree180();
void program_down();

int main(void){
	wiringPiSetup();

	pinMode(sw1, INPUT);
	pinMode(sw2, INPUT);
	pinMode(sw3, INPUT);
	pinMode(sw4, INPUT);

	pinMode(STEP_OUTA, OUTPUT);
	pinMode(STEP_OUTB, OUTPUT);
	pinMode(STEP_OUT2A, OUTPUT);
	pinMode(STEP_OUT2B, OUTPUT);

	digitalWrite(STEP_OUTA, 0);
	digitalWrite(STEP_OUTB, 0);
	digitalWrite(STEP_OUT2A, 0);
	digitalWrite(STEP_OUT2B, 0);

	printf("Step Motor Control Start!!\n");
	printf("SW1 : 45도\nSW2 : 90도\nSW3 : 180도\nSW4 : Exit\n");

	while(1) {
		if(digitalRead(sw1) == 0) degree45();
		else if(digitalRead(sw2) == 0) degree90();
		else if(digitalRead(sw3) == 0) degree180();
		else if(digitalRead(sw4) == 0) program_down();
	}

	return 0;
}

void degree45() {
	printf("45도 회전합니다!!\n");
	for(int i=0;i<67;i++) {
		digitalWrite(STEP_OUTA, 1);
		usleep(2000);
		digitalWrite(STEP_OUTA, 0);
		digitalWrite(STEP_OUTB, 1);
		usleep(2000);
		digitalWrite(STEP_OUTB, 0);
		digitalWrite(STEP_OUT2A, 1);
		usleep(2000);
		digitalWrite(STEP_OUT2A, 0);
		digitalWrite(STEP_OUT2B, 1);
		usleep(2000);
		digitalWrite(STEP_OUT2B, 0);
	}
}

void degree90() {
	printf("90도 회전합니다!!\n");
	for(int i=0;i<133;i++) {
		digitalWrite(STEP_OUTA, 1);
		usleep(2000);
		digitalWrite(STEP_OUTA, 0);
		digitalWrite(STEP_OUTB, 1);
		usleep(2000);
		digitalWrite(STEP_OUTB, 0);
		digitalWrite(STEP_OUT2A, 1);
		usleep(2000);
		digitalWrite(STEP_OUT2A, 0);
		digitalWrite(STEP_OUT2B, 1);
		usleep(2000);
		digitalWrite(STEP_OUT2B, 0);
	}
}

void degree180() {
	printf("180도 회전합니다!!\n");
	for(int i=0;i<268;i++) {
		digitalWrite(STEP_OUTA, 1);
		usleep(2000);
		digitalWrite(STEP_OUTA, 0);
		digitalWrite(STEP_OUTB, 1);
		usleep(2000);
		digitalWrite(STEP_OUTB, 0);
		digitalWrite(STEP_OUT2A, 1);
		usleep(2000);
		digitalWrite(STEP_OUT2A, 0);
		digitalWrite(STEP_OUT2B, 1);
		usleep(2000);
		digitalWrite(STEP_OUT2B, 0);
	}
}

void program_down() {
		printf("프로그램을 종료합니다.\n");
		exit(0);
}
