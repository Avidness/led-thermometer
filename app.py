from sense_hat import SenseHat
from helpers import weather_images as images, colors
import urllib.request, json, threading, yaml

class PixelColor: 
  def __init__(self, r, g, b):
    self.r = r
    self.g = g
    self.b = b

def run(interval, url):
  threading.Timer(interval, run, [interval, url]).start()
  tempF = get_temp(url)
  set_display(tempF)

def get_temp(url):
  resp = urllib.request.urlopen(url)
  data = resp.read()
  encoding = resp.info().get_content_charset('utf-8')
  jdata = json.loads(data.decode(encoding))
  
  tempC = jdata['main']['temp']
  tempF = (tempC * 9/5) + 32
  return str(int(round(tempF + .5)))

def set_display(tempF):
  print(tempF)
  sense = SenseHat()
  sense.set_rotation(180)

  color = get_color(tempF)

  top = 7
  bot = 0
  test = images.test_image(colors.g)
  sense.set_pixels(test)
  sense.set_pixel(top, bot, color.r, color.b, color.g)

def get_color(tempF):
  #red = 255,0,0
  #blue = 0,0,255
  return PixelColor(0,0,255)

with open('config.yml', 'r') as file:
  config = yaml.load(file, Loader=yaml.FullLoader)

api_url = "%s?lat=%s&lon=%s" % (config['url'], config['lat'], config['lon'])
run(config['secInterval'], api_url)
