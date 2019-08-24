from sense_hat import SenseHat
from helpers import weather_images as images, colors
import urllib.request, json, threading, yaml

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
  image = images.test_image(color)
  sense.set_pixels(image)

def get_color(tempF):
  tempF = float(tempF)
  if tempF > 80:
    return colors.red
  elif tempF > 75:
    return colors.orange
  elif tempF > 70:
    return colors.yellow
  elif tempF > 65: 
    return colors.green
  elif tempF > 60:
    return colors.violet
  elif tempF > 45:
    return colors.indigo
  elif tempF > 40:
    return colors.blue
  else:
    return colors.white

with open('config.yml', 'r') as file:
  config = yaml.load(file, Loader=yaml.FullLoader)

api_url = "%s?lat=%s&lon=%s" % (config['url'], config['lat'], config['lon'])
run(config['secInterval'], api_url)
