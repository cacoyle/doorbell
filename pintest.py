import i2c_lcd_driver
import RPi.GPIO as GPIO
import time

mylcd = i2c_lcd_driver.lcd()

def dingdong(ctx):
    print("doorbell pressed")
    mylcd.lcd_display_string("doorbell pressed", 1)

def clearlcd():
    mylcd.lcd_clear()

doorbell = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(doorbell, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.add_event_detect(doorbell, GPIO.RISING, callback=dingdong, bouncetime=300)
# GPIO.add_event_detect(doorbell, GPIO.FALLING, callback=clearlcd, bouncetime=300)

try:
    while(True):
        print("Waiting for press...")
        time.sleep(1)
        if not GPIO.input(doorbell):
            mylcd.lcd_clear()
    
    
except KeyboardInterrupt:
    GPIO.cleanup()
