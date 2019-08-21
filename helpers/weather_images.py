from .colors import *
 
def test_image(color):
  r = color.rgb
  e = empty.rgb
  return [
    e,e,e,e,e,e,e,e,
    e,e,r,r,r,r,e,e,
    e,r,r,r,r,r,r,e,
    e,r,r,e,e,r,r,e,
    e,r,r,e,e,r,r,e,
    e,r,r,r,r,r,r,e,
    e,e,r,r,r,r,e,e,
    e,e,e,e,e,e,e,e
  ];
