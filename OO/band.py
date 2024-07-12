from instruments import Instrument, InstrumentKind, Distorcion, Guitar, Flute, EletricGuitar


gianini = Guitar("Giannini m2", kind=InstrumentKind.keys)
print(gianini.play())
print(gianini.colors)

yamaha = Flute("Yamaha Magic Flute", colors=["silver"])
print(yamaha.play())
print(yamaha.colors)


lespaul = EletricGuitar("lespaul m1")
print(lespaul.play(distorcion=Distorcion.whisper))
