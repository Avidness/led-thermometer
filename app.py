from sense_hat import SenseHat
from helpers import led_images as images
import urllib.request, json, threading, yaml

def run(interval, url):
  threading.Timer(interval, run, [interval, url]).start()
  req_temp(url)

def req_temp(url):
  resp = urllib.request.urlopen(url)
  data = resp.read()
  encoding = resp.info().get_content_charset('utf-8')
  jdata = json.loads(data.decode(encoding))
  
  tempC = jdata['main']['temp']
  tempF = (tempC * 9/5) + 32

  set_display(str(int(round(tempF + .5))))

def set_display(tempF):
  print(tempF)
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
  config = yaml.load(file, Loader=yaml.FullLoader)

api_url = "%s?lat=%s&lon=%s" % (config['url'], config['lat'], config['lon'])
run(config['secInterval'], api_url)
