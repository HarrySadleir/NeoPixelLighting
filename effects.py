import utils
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

# Initialize pixels object
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

# INPUTS: 
#   - width: the number of pixels to be taken as one complete loop
#   - wait: the time between each step. (This+calculationtime)*255=total time of this function
# EFFECTS:
#   - produces a rainbow that moves along the strip
def rainbow_cycle(wait=0.001, width=num_pixels):
    for i in range(255):
        rainbow(i, wait)
        

def rainbow(i, wait=0.001, width=num_pixels):
    for j in range(num_pixels):
        x = int((j % width) * 256. / width)
        x = x + i & 255
        pixels[j] = utils.wheel(x)
    pixels.show()
    time.sleep(wait)

# EFFECTS:
#   - Neatly turns off pixels and cleanup GPIO usage
def cleanup():
    try:
        pixels.deinit()
    except:
        time.sleep(1)
        print("Cleaned up GPIO resources.")
    

# EFFECTS: sets the pixels to a single colour
def solid(r, g, b):
    pixels.fill((r, g, b))
    pixels.show()

    