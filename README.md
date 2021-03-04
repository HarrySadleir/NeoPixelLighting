
# NeoPixel Lighting for Raspberry Pi

  

  

This personal project uses RaspberryPi and Python as a control for individually addressable RGB LEDs, also known as Neopixels or WS2182b lights. The project is currently in a prototyping and coding phase, using a breadboard to connect all necessary components while testing various python, bash, and web scripts to control the lighting.

## Usage
1. Use the command line app main.py. This can be automated by placing bash_scripts/bootup in /etc/rc.local:
 - *-cleanup*: runs pixels.deinit() and exits
 - *-solid r g b*: sets the
 - *-loop_rc wait width*: loops rainbow cycle with sleep interval: wait and period: width
 2. Using the web application:
 - Setup the Flask web app as described in [Naztronaut's amazing tutorials](https://github.com/naztronaut/RaspberryPi-browser-led-control)
 - Run consumer.py, which can be automated again by utilizing /etc/rc.local

## Components

  

1. Raspberry Pi

  

- I use Rasberry Pi 3b, but I plan to use a simpler Pi in the future to lower power usage

  

2. WS2812b LED Strip

  

3. 5V power supply

  

4. Required wiring components

  

-  [I used this guide for wiring the NeoPixels](https://www.thegeekpub.com/15990/wiring-ws2812b-addressable-leds-to-the-raspbery-pi/)

  

- Push button to use as a power button

  

  

## Tools

  

1. Python

  

-  [Adafruit NeoPixels on Raspberry Pi](https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage)

  

- RPi.GPIO

2. Bash

- /etc/rc.local for running a bootup script for the NeoPixel and power button on startup

- A safe shutdown script for the NeoPixel called when the power button is pressed

  

3. Web development tools: Apache2, Flask, HTML, CSS, Javascript

- This part of the project's code has been taken from [Naztronaut also known as EasyProgramming](https://github.com/naztronaut/RaspberryPi-browser-led-control), and I will soon be modifying it to suite my needs 

  

4. Rabbitmq with the Python library Pika

- The use of Rabbitmq is different from Naztronaut's project, adafruit's neopixel library requires root priviledges, thus required this work around