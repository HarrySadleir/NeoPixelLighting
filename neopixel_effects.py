import neopixel_utils as utils
import time
import board
import neopixel
import RPi.GPIO

# Use GPIO pin 18
pixel_pin = board.D18

# The number of pixels
num_pixels = 300

# Set the order of neopixel's expected input
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

# INPUTS: 
#   - width: the number of pixels to be taken as one complete loop
#   - wait: the time between each step. (This+calculationtime)*255=total time of this function
# EFFECTS:
#   - produces a rainbow that moves along the strip
def rainbow_cycle(wait=0.001, width=num_pixels):
    print(width)
    for i in range(255):
        for j in range(num_pixels):
            x = int((j % width) * 256. / width)
            x = x + i & 255
            pixels[j] = utils.wheel(x)
        pixels.show()
        time.sleep(wait)

def cleanup():
    pixels.fill((0,0,0))
    pixels.show()
    RPi.GPIO.cleanup()
    print("\nCleaned up GPIO resources.")



    