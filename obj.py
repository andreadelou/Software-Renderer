import struct 

def color(r, g, b):
    r = int(min(255, max(r, 0)))
    g = int(min(255, max(g, 0)))
    b = int(min(255, max(b, 0)))
    return bytes([b, g, r])


class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()
            self.vertices = []
            self.tvertices = []
            self.vfaces = []
            self.normals = []
            self.read()

    def read(self):
        for line in self.lines:
            if line:
                try:
                    prefix, value = line.split(' ', 1)
                except:
                    prefix = ''
                if prefix == 'v':
                    self.vertices.append(list(map(float, value.split(' '))))
                if prefix == 'vt':
                    self.tvertices.append(list(map(float, value.split(' ')))) 
                if prefix == 'vn':
                    self.normals.append(list(map(float, value.split(' '))))                   
                elif prefix == 'f':
                    try:
                        self.vfaces.append([list(map(int , face.split('/'))) for face in value.split(' ')])
                    except:
                        self.vfaces.append([list(map(int , face.split('//'))) for face in value.split(' ')])


class Texture(object):
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        with open(self.path, "rb") as image:
            image.seek(10)
            headerSize = struct.unpack('=l', image.read(4))[0]

            image.seek(14 + 4)
            self.width = struct.unpack('=l', image.read(4))[0]
            self.height = struct.unpack('=l', image.read(4))[0]

            image.seek(headerSize)

            self.pixels = []

            for y in range(self.height):
                self.pixels.append([])
                for x in range(self.width):
                    b = ord(image.read(1)) / 255
                    g = ord(image.read(1)) / 255
                    r = ord(image.read(1)) / 255

                    self.pixels[y].append( color(r,g,b) )

    def getColor(self, tx, ty, intensity = 1):
        if 0<=tx<1 and 0<=ty<1:
            x = int(tx * self.width)
            y = int(ty * self.height)
            return self.pixels[y][x]
        else:
            return color(0,0,0)