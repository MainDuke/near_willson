import time
import board
import neopixel

# 핀 설정 (Jetson 보드의 사용 가능한 PWM 핀)
pixel_pin = board.D18

# NeoPixel 스트립의 LED 개수
num_pixels = 30

# NeoPixel 객체 생성
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB)

def colorWipe(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        pixels.show()
        time.sleep(wait)

try:
    while True:
        # 빨간색으로 전환
        colorWipe((255, 0, 0), 0.1)  # Red
        # 녹색으로 전환
        colorWipe((0, 255, 0), 0.1)  # Green
        # 파란색으로 전환
        colorWipe((0, 0, 255), 0.1)  # Blue

except KeyboardInterrupt:
    pixels.fill((0, 0, 0))
    pixels.show()
