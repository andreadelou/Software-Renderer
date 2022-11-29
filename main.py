from lib import Render
from Vector import V3
from Obj import *

r = Render()

r.glCreateWindow(1024, 1024)

r.lightPosition(0, 0, 1)

textura = Texture('./pared.bmp')
r.load('plano.obj',translate=(0,800,-300), scale=(70,90,50), texture=textura)
textura = Texture('./pared.bmp')
r.load('plano.obj',translate=(600,800,-300), scale=(70,90,50), texture=textura)
textura = Texture('./couch.bmp')
r.load('./couch.obj', translate=[730, 200, -800], scale=[200, 200, 200], texture=textura)
textura = Texture('./green.bmp')
r.load('./maceta.obj', translate=[250, 200, -300], scale=[100, 100, 100], texture=textura)
textura = Texture('./perro.bmp')
r.load('./perro.obj', translate=[380, 200, -500], scale=[500, 500, 500], texture=textura)
textura = Texture('./amarillo.bmp')
r.load('./lamp.obj', translate=[512, 650, -800], scale=[400, 400, 400], texture=textura)
textura = Texture('./cafe.bmp')
r.load('./mesa.obj', translate=[140, 150, -800], scale=[50, 50, 50], texture=textura)

r.glFinish('out.bmp')
