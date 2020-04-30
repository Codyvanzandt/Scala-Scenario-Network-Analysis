from dataclasses import dataclass
from enum import Enum


class Archetype(Enum):
    VECCHI = 0
    INNAMORATI = 1
    SERVI = 2
    CAPITANI = 3


class Gender(Enum):
    MALE = 0
    FEMALE = 1


@dataclass
class Character:
    name: str
    archetype: Archetype
    gender: Gender


# VECCHI
PANTALONE = Character("Pantalone", Archetype.VECCHI, Gender.MALE)
GRAZIANO = Character("Graziano", Archetype.VECCHI, Gender.MALE)
TOFANO = Character("Tofano", Archetype.VECCHI, Gender.MALE)
CASSANDRO = Character("Cassandro", Archetype.VECCHI, Gender.MALE)
CATALDO = Character("Cataldo", Archetype.VECCHI, Gender.MALE)
CLAUDIONE = Character("Claudione", Archetype.VECCHI, Gender.MALE)
HIBRAHIM = Character("Hibrahim", Archetype.VECCHI, Gender.MALE)
LAURA = Character("Laura", Archetype.VECCHI, Gender.FEMALE)


# SERVI
PEDROLINO = Character("Pedrolino", Archetype.SERVI, Gender.MALE)
ARLECCHINO = Character("Arlecchino", Archetype.SERVI, Gender.MALE)
BURATTINO = Character("Burattino", Archetype.SERVI, Gender.MALE)
GRILLO = Character("Grillo", Archetype.SERVI, Gender.MALE)
CAVICCHIO = Character("Cavicchio", Archetype.SERVI, Gender.MALE)
PIOMBINO = Character("Piombino", Archetype.SERVI, Gender.MALE)
INNKEEPER = Character("Innkeeper", Archetype.SERVI, Gender.MALE)
FRANCESCHINA = Character("Franceschina", Archetype.SERVI, Gender.FEMALE)
PASQUELLA = Character("Pasquella", Archetype.SERVI, Gender.FEMALE)
OLIVETTA = Character("Olivetta", Archetype.SERVI, Gender.FEMALE)
RICCIOLINA = Character("Ricciolina", Archetype.SERVI, Gender.FEMALE)

# INNAMORATI
FLAVIO = Character("Flavio", Archetype.INNAMORATI, Gender.MALE)
ORAZIO = Character("Orazio", Archetype.INNAMORATI, Gender.MALE)
CINZIO = Character("Cinzio", Archetype.INNAMORATI, Gender.MALE)
FABRIZIO = Character("Fabrizio", Archetype.INNAMORATI, Gender.MALE)
FLAMINIA = Character("Flaminia", Archetype.INNAMORATI, Gender.FEMALE)
ISABELLA = Character("Isabella", Archetype.INNAMORATI, Gender.FEMALE)
LIDIA = Character("Lidia", Archetype.INNAMORATI, Gender.FEMALE)
FLAVIA = Character("Flavia", Archetype.INNAMORATI, Gender.FEMALE)
SILVIA = Character("Silvia", Archetype.INNAMORATI, Gender.FEMALE)

# CAPITANI
CAPITANO = Character("Capitano", Archetype.CAPITANI, Gender.MALE)
VITTORIA = Character("Vittoria", Archetype.CAPITANI, Gender.FEMALE)

_NICKNAME_TO_CHARACTER = {
    "Arle": ARLECCHINO,
    "Bur": BURATTINO,
    "Cap": CAPITANO,
    "Cas": CASSANDRO,
    "Cat": CATALDO,
    "Cavi": CAVICCHIO,
    "Clau": CLAUDIONE,
    "Cinz": CINZIO,
    "Fabr": FABRIZIO,
    "Flam": FLAMINIA,
    "Flav": FLAVIO,
    "Flavia": FLAVIA,
    "Fran": FRANCESCHINA,
    "Graz": GRAZIANO,
    "Gril": GRILLO,
    "Hibr": HIBRAHIM,
    "Inn": INNKEEPER,
    "Isa": ISABELLA,
    "Lau": LAURA,
    "Lid": LIDIA,
    "Oliv": OLIVETTA,
    "Oraz": ORAZIO,
    "Pant": PANTALONE,
    "Pasq": PASQUELLA,
    "Pedr": PEDROLINO,
    "Pio": PIOMBINO,
    "Ric": RICCIOLINA,
    "Silv": SILVIA,
    "Tof": TOFANO,
    "Vit": VITTORIA,
}


def get_character(nickname):
    return _NICKNAME_TO_CHARACTER[nickname]
