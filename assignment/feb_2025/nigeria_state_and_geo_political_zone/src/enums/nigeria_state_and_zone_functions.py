from src.enums.nigeria_state_and_zone import NigeriaStateGeoPoliticalZones as NgStateGeoPolZones

def get_geo_political_zone_by_state(state_name:str) -> NgStateGeoPolZones:
    for zone in NgStateGeoPolZones:
        for state in zone.value:
            if state.lower() == state_name.lower():
                return zone
    raise ValueError (f"'{state_name}' is not a valid state name")
