from instruments import Guitar, Flute, EletricGuitar, Distorcion

gianini = Guitar("Gianini m2", colors=["wood"])
print(gianini.play())
print(gianini.colors)

yamaha = Flute("Yamaha Magic Flute", colors=["silver"])
print(yamaha.play())
print(yamaha.colors)

lespaul = EletricGuitar("Les Paul 2001")
print(lespaul.play(distortion=Distorcion.wave))
