from flask import Flask, request, jsonify
import pika
import os

app = Flask(__name__)

# Starts the consumer program consumer.py with super user priviledges
os.system("sudo /home/pi/projects/neopixel_project/bash_scripts/bootup")


@app.route('/', methods=['GET'])
def rainbow():
    # Retrieve status from Flask via get
    status = request.args.get('status')

    # Open rabbitmq channel, preparing to send a message
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    channel = connection.channel()
    channel.queue_declare(queue='commandq')

    if status == "rc":
        channel.basic_publish(
            exchange='', routing_key='commandq',
            body='rainbowcycle'
        )
        return jsonify({"message": "Neopixels set to rainbow"})
    elif status == "off":
        channel.basic_publish(
            exchange='',routing_key='commandq',
            body='off'
        )
        return jsonify({"message": "Neopixels have been slept"})
    else:
        return jsonify({"message": "Not a valid status"})
