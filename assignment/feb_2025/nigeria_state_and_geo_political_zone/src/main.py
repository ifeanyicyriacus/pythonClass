from enums.nigeria_state_and_zone_functions import get_geo_political_zone_by_state

print("Find Geo Political Zone By State Name")
response: str = input("Enter state name: ")

try:
    zone:str = str(get_geo_political_zone_by_state(response))
    print(f"'{response}' state belongs to '{zone}' geo political zone")
except ValueError as e:
    print(e)

