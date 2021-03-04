#!/usr/bin/env python3
#A consumer that monitors a rabbitmq queue named commandq for commands
#This producer for this queue is a Flask app that echoes
import pika
import time
import effects

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()
channel.queue_declare(queue='commandq')


def activate(command, it):
    if command == 'rainbowcycle':
        effects.rainbow(it)
        it += 1
    if command == 'off':
        effects.solid(0,0,0)
        time.sleep(1)
    


if __name__ == "__main__":
    # variable of the last command received, used in case no signal is sent
    # initial state will be first command called
    lastcommand = 'off'

    # variable for time dependant iteration
    it = 0
    
    while(True):
        method_frame, header_frame, body = channel.basic_get(queue = 'commandq')
        if method_frame:
            lastcommand = body.decode()
            channel.basic_ack(method_frame.delivery_tag)
            print(lastcommand)

        activate(lastcommand, it)
        it += 1
        if it > 255:
            it = 0


        