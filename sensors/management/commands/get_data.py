import datetime
import json

from django.core.management import BaseCommand
import paho.mqtt.client as mqtt
from sensors.serializers import WalkinDataSerializer, AbdominalDataSerializer


def on_connect(client, userdata, flags, rc):
    print("Se conecto con mqtt " + str(rc))
    client.subscribe("#")


def on_message(client, userdata, msg):
    print(datetime.datetime.now(),"Message", "str(msg.payload)}", "recieved.")
    if msg.topic == "abs":
        print(datetime.datetime.now(), "Message is for abdominals")
        serializer = AbdominalDataSerializer(
            data=json.loads(msg.payload)
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(datetime.datetime.now(), "data was saved")
    if msg.topic == "steps":
        print(datetime.datetime.now(), "Message is for steps")
        serializer = WalkinDataSerializer(
            data=json.loads(msg.payload)
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(datetime.datetime.now(), "data was saved")



class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        ##mqtt://warpdancer648:A1dab69XaFtTgLSJ@warpdancer648.cloud.shiftr.io
        client.username_pw_set("warpdancer648", "A1dab69XaFtTgLSJ")
        client.connect("warpdancer648.cloud.shiftr.io", 1883, 60)
        client.loop_forever()
