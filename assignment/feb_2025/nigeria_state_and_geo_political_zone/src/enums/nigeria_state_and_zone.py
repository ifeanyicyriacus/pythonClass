from enum import Enum

class NigeriaStateGeoPoliticalZones(Enum):
    NORTH_CENTRAL = "Benue", "FCT", "Kwara", "Nasarawa", "Niger", "Plateau"
    NORTH_EAST = "Adamawa", "Bauchi", "Brono", "Gombe", "Taraba", "Yobe"
    NORTH_WEST = "Kaduna", "Katisna", "Kano", "Kebbi", "Sokoto", "Jigwa", "Zamfara"
    SOUTH_EAST = "Abia", "Anambra", "Ebonyi", "Enugu", "Imo"
    SOUTH_SOUTH = "Akwa-Ibom", "Bayelsa", "Cross-River", "Delta", "Edo", "Rivers"
    SOUTH_WEST = "Ekiti", "Lagos", "Osun", "Ondo", "Ogun", "Oyo"

    def __init__(self, *states:str):
        self.__states = states

    @property
    def states(self) -> tuple:
        return self.__states

    def __str__(self):
        return (self.name
                .title()
                .replace("_","-"))