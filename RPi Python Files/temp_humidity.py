# import Adafruit_DHT *** Install package on raspberry pis

# DHT_PIN is the GPIO pin that the temp sensor is connected to, change according to rpi config
def get_temperature_humidity(DHT_PIN = 4):
    DHT_SENSOR = Adafruit_DHT.DHT_22

    humidity, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    humidity = humidity if humidity is not None else '-'
    temp = temp if temp is not None else '-'

    return {'humidity': humidity, 'temp': temp}

    