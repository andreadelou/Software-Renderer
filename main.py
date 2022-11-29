from lib import Render
from Vector import V3
from Obj import *

r = Render()

r.glCreateWindow(1024, 1024)

r.lightPosition(0, 0, 1)
    
textura = Texture('./couch.bmp')
r.load('./couch.obj', translate=[730, 200, -800], scale=[200, 200, 200], texture=textura)
textura = Texture('./green.bmp')
r.load('./maceta.obj', translate=[250, 200, -300], scale=[100, 100, 100], texture=textura)
textura = Texture('./perro.bmp')
r.load('./perro.obj', translate=[380, 200, -500], scale=[500, 500, 500], texture=textura)
r.glFinish('out.bmp')
