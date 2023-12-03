# import RPi.GPIO as GPIO
from datetime import datetime
import time
from temp_humidity import get_temperature_humidity
from gps import get_gps_location
from thermal_cam import get_thermal_cam_pic

import serial

def main_loop(file_name: str, use_thermal_camera: bool = False):
    with open(file_name, 'a') as file:
        # If file is empty, add the header row
        if not file.read(1):
            file.write('Time,Latitude,Longitude,Temperature,Humidity\n')
        
        start_time = time.time()
        while True:
            current_datetime = datetime.now().strftime()

            # Get GPS location -- TODO: Change to proper serial of the GPS module
            gps_serial = serial.Serial("/dev/ttyS0")
            current_location = get_gps_location(gps_serial)

            # Get temperature and humidity
            DHT_PIN = 4
            current_temp_humidity = get_temperature_humidity(DHT_PIN=DHT_PIN)

            # Take picture of thermal camera (only if use_thermal+camera is true)
            if use_thermal_camera:
                get_thermal_cam_pic(current_datetime)

            # Write these values into the file
            file.write(f"{current_datetime},{current_location['lat']},{current_location['long']},{current_temp_humidity['temp']},{current_temp_humidity['humidity']}\n")

            # Turn on LED

            # Turn off LED

            # Run this loop every 5 seconds
            time.sleep(5.0 - (time.time() - start_time) % 5.0)

if __name__ == "__main__":
    main_loop('VHS Thesis Data.csv', False)