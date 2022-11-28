from lib import Render
from Vector import V3
from Obj import *

r = Render()

r.glCreateWindow(800, 800)

r.lightPosition(0, 0, 1)
    
textura = Texture("./bench.bmp")

r.load("./bench.obj", translate=[512, 512, 0], scale=[0.00001, 0.00001, 0.00001], texture=textura)

r.glFinish('out.bmp')
