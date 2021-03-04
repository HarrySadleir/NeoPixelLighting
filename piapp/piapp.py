from flask import Flask, request, jsonify
import pika

app = Flask(__name__)


@app.route('/', methods=['GET'])
def rainbow():
    status = request.args.get('status')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    channel = connection.channel()
    channel.queue_declare(queue='commandq')

    if status == "on":
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
