# Abstração e Herança com dataclasse?
# Tem enum no Python? Enum - Enumeração / Enumerador
# dataclasses com valor default dão erro
# para que serve o super()?

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum

# class ABCInstrument(ABC):
#
#    @abstractmethod
#    def play(self):
#        ...
#
#
# @dataclass
# class DataInstrumentMixin():  # deve ser usado junto com outra classe
#    name: str
#    kind: str
#    sound: str


# Enum
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
    kind: InstrumentKind
    sound: str
    colors: list[str] = field(default_factory=list)

    @abstractmethod
    def play(self):
        ...


@dataclass
class Guitar(Instrument):
    n_strings: int = 6
    sound: str = "Ding Ding Ding"
    kind: InstrumentKind = InstrumentKind.string
    colors: list[str] = field(default_factory=lambda: ["Red", "Black"])

    def play(self):
        return self.sound


@dataclass
class EletricGuitar(Guitar):
    sound: str = "Wah Wah Wah"

    def play(self, distortion: Distorcion = Distorcion.wave):
        return_from_base_class = super().play()
        if distortion is Distorcion.wave:
            return "~~~".join(return_from_base_class.split())
        elif distortion is Distorcion.whisper:
            return "...".join(return_from_base_class.split())

        return return_from_base_class


@dataclass
class Flute(Instrument):
    sound: str = "Flu Flu Flu"
    kind: InstrumentKind = InstrumentKind.wind
    colors: list[str] = field(default_factory=lambda: ["Beige", "White"])

    def play(self):
        return self.sound
