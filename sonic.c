#include <stdio.h>
#include <wiringPi.h>

#define PIN_LED 4
#define PIN_ECHO 23
#define PIN_TRIG 24

int main(void)
{

    wiringPiSetup();
	wiringPiSetupGpio();

	pinMode(PIN_ECHO, INPUT);
	pinMode(PIN_TRIG, OUTPUT);
	pinMode(PIN_LED, OUTPUT);

	digitalWrite(PIN_TRIG, LOW);
	delay(30);
	while(1)
	{
		digitalWrite(PIN_TRIG, HIGH);
		delayMicroseconds(20);
		digitalWrite(PIN_TRIG, LOW);

		while(digitalRead(PIN_ECHO) ==LOW);


		long startTime = micros();

		while(digitalRead(PIN_ECHO)== HIGH);
		long endTime = micros() - startTime;


		int distance = endTime/58;
        printf("distance = %d\n",distance);

		if(distance <30)
		{
			digitalWrite(PIN_LED, HIGH);
            printf("HIGH\n");
		}
		else
		{
			digitalWrite(PIN_LED, LOW);
            printf("LOW\n");
		}
		delay(1000);
	}
	return 0;
}