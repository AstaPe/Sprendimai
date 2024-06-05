from paskaita_18.figuros import Staciakampis, Trikampis, Apskritimas

if __name__ == "__main__":
    apskritimas = Apskritimas(radius=5)
    print(f"Apskritimo plotas: {apskritimas.plotas():.2f}")
    print(f"Apskritimo perimetras: {apskritimas.perimetras():.2f}")

    staciakampis = Staciakampis(ilgis=4, plotis=7)
    print(f"Stačiakampio plotas: {staciakampis.plotas():.2f}")
    print(f"Stačiakampio perimetras: {staciakampis.perimetras():.2f}")

    trikampis = Trikampis(a=3, b=4, c=5)
    print(f"Trikampio plotas: {trikampis.plotas():.2f}")
    print(f"Trikampio perimetras: {trikampis.perimetras():.2f}")
