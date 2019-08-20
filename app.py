from sense_hat import SenseHat
from helpers import led_images as images
import urllib, json, threading, yaml

def req_temp(url):
  threading.Timer(5.0, req_temp, [url]).start()

  resp = urllib.urlopen(url)
  data = json.loads(resp.read())
  
  tempC = data['main']['temp']
  tempF = (tempC * 9/5) + 32

  set_display(str(int(round(tempF + .5))))

def set_display(tempF):
  print tempF
  sense = SenseHat()
  sense.set_rotation(180)
  sense.show_message(tempF)

  #top = 7
  #bot = 0
  #red = 255,0,0
  #blue = 0,0,255

  sense.set_pixels(images.cat_eyes_open)
  sense.set_pixel(0,7, 255,255,255)

with open('config.yml', 'r') as file:
  config = yaml.load(file)

print config
print config['lat']
print config.url
lat = 40.76
lon = -73.98
api_url = 'https://fcc-weather-api.glitch.me/api/current?lat=%s&lon=%s' % (lat, lon)
req_temp(api_url)
