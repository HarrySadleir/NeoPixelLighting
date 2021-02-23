import neopixel_effects as effects

try:
    while True:
        effects.rainbow_cycle() 
        #effects.rainbow_loop()
except KeyboardInterrupt:
    effects.cleanup()
    
    