from paskaita_18.pratimai import Shape
import math


class Staciakampis(Shape):
    def __init__(self, ilgis, plotis):
        self.ilgis = ilgis
        self.plotis = plotis

    def plotas(self):
        return self.ilgis * self.plotis

    def perimetras(self):
        return 2 * (self.ilgis + self.plotis)


class Trikampis(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def plotas(self):
        # Naudojame Herono formulę plotui apskaičiuoti
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimetras(self):
        return self.a + self.b + self.c
