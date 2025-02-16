from enums.nigeria_state_and_zone import NigeriaStateGeoPoliticalZones as ng_state_geo_pol_zones

def get_geo_political_zone_by_state(state_name:str) -> ng_state_geo_pol_zones:
    for zone in ng_state_geo_pol_zones:
        for state in zone.value:
            if state.lower() == state_name.lower():
                return zone
    raise ValueError (f"'{state_name}' is not a valid state name")
