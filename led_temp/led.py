import lgpio
import time

# lgpio 핸들 열기 (gpiochip0은 보통 기본적으로 사용되는 GPIO 핀)
handle = lgpio.gpiochip_open(0)

# GPIO 14번을 출력 모드로 설정
lgpio.gpio_claim_output(handle, 14)

try:
    while True:
        lgpio.gpio_write(handle, 14, 0)  # LOW
        time.sleep(2)
        lgpio.gpio_write(handle, 14, 1)  # HIGH
        time.sleep(2)
except KeyboardInterrupt:
    print("프로그램 종료")
finally:
    # 핸들 닫기
    lgpio.gpiochip_close(handle)