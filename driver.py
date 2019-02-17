import Adafruit_DHT

from gardnr import drivers


class Dht22(drivers.Sensor):
    """
    config:
        pin: the GPIO pin number
    """
    MAX_ATTEMPTS = 2

    def read(self):

        for _ in range(DHT22.MAX_ATTEMPTS):
            sensor = Adafruit_DHT.DHT22

            # Try to grab a sensor reading. Use the read_retry method which
            # will retry up to 15 times to get a sensor reading
            # (waiting 2 seconds between each retry).
            humidity, temperature = Adafruit_DHT.read_retry(sensor, self.pin)

            # Note that sometimes you won't get a reading and
            # the results will be null (because Linux can't
            # guarantee the timing of calls to read the sensor).
            # If this happens try again!
            if humidity is not None and temperature is not None:
                self.create_metric_log('air-temp', temperature)
                self.create_metric_log('rh', humidity)
                return

            raise IOError('Cannot read from DHT22')
