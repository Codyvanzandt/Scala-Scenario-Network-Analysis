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
