# DHT22 air temperature and relative humidity

Compatible with both Raspberry Pi and Beaglebone Black

[Datasheet](https://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.pdf)
[Tutorial](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/overview)

```
python3 -m pip install -r dht22/requirements.txt

gardnr add metric air temperature air-temp
gardnr add metric air humidity rh

gardnr add driver dht22 dht22.driver.py:Dht22 -c pin=13
```
