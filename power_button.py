# A script to run bash_scripts/haltshutdown when button on GPIO 16 is pressed

from gpiozero import Button 
import time 
import os 


if __name__ == "__main__":
    stopButton = Button(16) 

    while True: 
        if stopButton.is_pressed: #Check to see if button is pressed
            time.sleep(0.5) # wait for the hold time we want. 
            if stopButton.is_pressed: #check if the user let go of the button
                os.system("bash_scripts/haltshutdown") #shut down the Pi -h is or -r will reset
        time.sleep(1) # wait to loop again so we don’t use the processor too much.