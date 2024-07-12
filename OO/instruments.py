from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum


# Enumeração / Enumerador
class InstrumentKind(str, Enum):
    string = "string"
    wind = "wind"
    keys = "keys"
    drums = "drums"


class Distorcion(str, Enum):
    wave = "wave"
    whisper = "whisper"


@dataclass
class Instrument(ABC):
    name: str
    sound: str
    kind: InstrumentKind
    colors: list[str] = field(default_factory=list)

    @abstractmethod
    def play(self):
        ...


@dataclass
class Guitar(Instrument):
    n_strings: int = 6
    sound: str = "Ding Ding Ding"
    kind: InstrumentKind = InstrumentKind.string
    colors: list[str] = field(default_factory=lambda: ["red", "black"])

    def play(self):
        return self.sound


@dataclass
class EletricGuitar(Guitar):
    n_strings: int = 6
    sound: str = "Wah Wah Wah"

    def play(self, distorcion: Distorcion = Distorcion.wave):
        return_from_base_class = super().play()
        if distorcion is Distorcion.wave:
            return "~~~".join(return_from_base_class.split())
        if distorcion is Distorcion.whisper:
            return "...".join(return_from_base_class.split())

        return return_from_base_class

@dataclass
class Flute(Instrument):
    sound: str = "Flu Flu Flu"
    kind: InstrumentKind = InstrumentKind.wind
    colors: list[str] = field(default_factory=lambda: ["beige", "white"])

    def play(self):
        return self.sound
