import i2c_lcd_driver
import RPi.GPIO as GPIO
import time

mylcd = i2c_lcd_driver.lcd()

doorbell = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(doorbell, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

last_state = None
last_change = ""
last_poll = time.time()
try:
    while(True):
        poll_interval = time.time() - last_poll
        last_poll = time.time()
        # print(poll_interval)
        # print(GPIO.input(doorbell))
        if GPIO.input(doorbell):
           state = "PRESSED"
        else:
           state = "NOT PRESSED"
    
        if state != last_state:
            last_change = time.time()
            mylcd.lcd_clear()
            print("%s: %s" % (state, last_change))
            mylcd.lcd_display_string(state, 1)
    
        last_state = state
        # time.sleep(0.05)
except KeyboardInterrupt:
    GPIO.cleanup()


