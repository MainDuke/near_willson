import time
from rpi_ws281x import *

# LED 스트립 설정
LED_COUNT      = 2      # LED 개수
LED_PIN        = 12     # GPIO 핀 번호
LED_FREQ_HZ    = 800000 # LED 신호의 주파수 (800kHz)
LED_DMA        = 10     # DMA 채널을 사용
LED_BRIGHTNESS = 255    # LED 밝기 (0에서 255)
LED_INVERT     = False  # 신호 라인이 인버트되어야 할 경우 True로 설정

# LED 스트립 객체 생성
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

def colorWipe(strip, color, wait_ms=50):
    """모든 LED를 순차적으로 색상 변경."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

try:
    while True:
        # 빨간색으로 전환
        colorWipe(strip, Color(255, 0, 0))  # Red
        time.sleep(1)
        # 녹색으로 전환
        colorWipe(strip, Color(0, 255, 0))  # Green
        time.sleep(1)
        # 파란색으로 전환
        colorWipe(strip, Color(0, 0, 255))  # Blue
        time.sleep(1)

except KeyboardInterrupt:
    colorWipe(strip, Color(0,0,0), 10)
