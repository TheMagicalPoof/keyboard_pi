import RPi.GPIO as GPIO
import time

adjacency_s_r = [[None, None, None, None, "A"],
                 [None, "H", "K", "B", None],
                 ["I", "E", "C", "F", None],
                 ["G", "D", "J", None, None]]

read_pins = [7, 11, 13, 15, 19]
scan_pins = [21, 23, 29, 31]

GPIO.setmode(GPIO.BOARD)

is_emulate_mode = False

print(read_pins + scan_pins)

def read_event(r_pin_i):
    # now r_pin_i is HIGH
    for s_pin_i, s_pin in enumerate(scan_pins):
        if GPIO.input(s_pin) == GPIO.HIGH:
            print("Now pressed:{button}".format(button=adjacency_s_r[s_pin_i][r_pin_i]))

def main():
    GPIO.setup(read_pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(scan_pins, GPIO.IN)


    for r_pin_i, r_pin in enumerate(read_pins):
        GPIO.add_event_detect(r_pin,
                              GPIO.RISING,
                              callback=lambda plug: read_event(r_pin_i),
                              bouncetime=100)

    while True:
        time.sleep(60)
#    time.sleep(0.5)
#    print(list(map(lambda x: GPIO.input(x), read_pins + scan_pins)))

# GPIO.cleanup()



if __name__ == "__main__":
    main()
