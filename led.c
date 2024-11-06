#include <wiringPi.h>
#include <stdio.h>

#define LED_PIN 15

int main(void) {
    // WiringPi 초기화
    if (wiringPiSetup() == -1) {
        printf("WiringPi 초기화 실패!\n");
        return 1;
    }

    // LED 핀을 출력으로 설정
    pinMode(LED_PIN, OUTPUT);

    while (1) {
        digitalWrite(LED_PIN, HIGH); // LED 켜기
        delay(1000);                  // 1초 대기
        digitalWrite(LED_PIN, LOW);  // LED 끄기
        delay(1000);                  // 1초 대기
    }

    return 0;
}