import time
import Adafruit_DHT
import BlynkLib

# Blynk Authorization Token
BLYNK_AUTH = 'I4N5PJz4emNiJwP4n5GqmQeNnyckWyTA'

# Set up the sensor
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # GPIO pin where DHT11 is connected

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Function to read and send DHT11 data to Blynk
def read_and_send_data():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    
    if humidity is not None and temperature is not None:
        print(f'Temperature: {temperature}°C, Humidity: {humidity}%')
        
        # Send data to Blynk App (replace V1, V2 with actual virtual pins)
        blynk.virtual_write(1, temperature)  # Sending temperature to Virtual Pin V1
        blynk.virtual_write(2, humidity)     # Sending humidity to Virtual Pin V2
    else:
        print("Failed to retrieve data from the sensor")

# Main loop
while True:
    read_and_send_data()
    blynk.run()
    time.sleep(10)  # Delay to prevent flooding Blynk server
