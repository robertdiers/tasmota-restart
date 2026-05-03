#!/usr/bin/env python

import configparser
import os

# read config
config = configparser.ConfigParser()


def read():
    try:
        # read config
        config.read('tasmota-restart.ini')

        values = {}

        values["mqtt_broker"] = config['MqttSection']['mqtt_broker']
        values["mqtt_port"] = int(config['MqttSection']['mqtt_port'])
        values["mqtt_user"] = config['MqttSection']['mqtt_user']
        values["mqtt_password"] = config['MqttSection']['mqtt_password']
        if os.getenv('MQTT_BROKER', 'None') != 'None':
            values["mqtt_broker"] = os.getenv('MQTT_BROKER')
        if os.getenv('MQTT_PORT', 'None') != 'None':
            values["mqtt_port"] = int(os.getenv('MQTT_PORT'))
        if os.getenv('MQTT_USER', 'None') != 'None':
            values["mqtt_user"] = os.getenv('MQTT_USER')
        if os.getenv('MQTT_PASSWORD', 'None') != 'None':
            values["mqtt_password"] = os.getenv('MQTT_PASSWORD')

        values["tasmota_name"] = config['Device']['tasmota_name']
        if os.getenv('TASMOTA_NAME', 'None') != 'None':
            values["tasmota_name"] = os.getenv('TASMOTA_NAME')

        return values
    except Exception as ex:
        print("ERROR Config: ", ex)
