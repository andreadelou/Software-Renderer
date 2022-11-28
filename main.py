from lib import Render
from Vector import V3
from Obj import *

r = Render()

r.glCreateWindow(1000, 1000)

r.lightPosition(0, 0, 1)
    
textura = Texture('./green.bmp')

r.load('./couch.obj', translate=[512, 512, 0], scale=[0.001, 0.001, 0.01], texture=textura)

r.glFinish('out.bmp')
