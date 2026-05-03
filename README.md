# tasmota restart

send off on with cron to restart the consumer (I'm using it to restart my waterworks)

### Defaults

plaese check config in tasmota-restart.ini file, could be overridden by Docker env variables

### Docker usage

Environment variables (all can be overridden):

* MQTT_BROKER (default: 192.168.1.3)
* MQTT_PORT (default: 1883)
* MQTT_USER (default: admin)
* MQTT_PASSWORD (default: password)
* TASMOTA_NAME (default: tasmota_wasserwerk)
* CRON (mandatory, no default)

Example:
```
docker run -d --restart always \
  -e MQTT_PASSWORD=abc123 \
  -e TASMOTA_NAME=whatever \
  -e "CRON=0 6,12,18 * * *" \
  --name tasmotarestart ghcr.io/robertdiers/tasmota-restart:1.0.0
```
