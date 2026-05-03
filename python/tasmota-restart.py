#!/usr/bin/env python

from datetime import datetime
import time

import Config
import Tasmota


if __name__ == "__main__":
    # print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " START #####")
    try:
        conf = Config.read()

        device_name = conf['tasmota_name']
        mqtt_broker = conf['mqtt_broker']
        mqtt_port = conf['mqtt_port']
        mqtt_user = conf['mqtt_user']
        mqtt_password = conf['mqtt_password']

        # connect to the MQTT server and restart the device
        Tasmota.connect(mqtt_broker, mqtt_port, mqtt_user, mqtt_password)

        status = Tasmota.get(device_name, "Power", ["POWER"])
        if status.get("POWER") == "ON":
            Tasmota.off(device_name)
            time.sleep(5)
            Tasmota.on(device_name)
            ts = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(ts + " " + device_name + " restarted")
        else:
            ts = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(ts + " " + device_name + " already off, skipping restart")

        # print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " END #####")

    except Exception as ex:
        print("ERROR: ", ex)
