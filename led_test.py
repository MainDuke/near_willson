import Jetson.GPIO as GPIO
import time

# 사용할 핀 번호 설정 (BOARD 번호링 방식)
led_pin = 12

# 핀 설정
GPIO.setmode(GPIO.BOARD)  # BOARD 핀번호링 스키마 사용
GPIO.setup(led_pin, GPIO.OUT)  # 핀을 출력으로 설정

try:
    while True:
        # LED 켜기
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED ON")
        time.sleep(1)  # 1초 동안 대기

        # LED 끄기
        GPIO.output(led_pin, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)  # 1초 동안 대기

except KeyboardInterrupt:
    print("프로그램 종료")

finally:
    GPIO.cleanup()  # 사용한 GPIO 핀 초기화
