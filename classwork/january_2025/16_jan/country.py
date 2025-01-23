def update_country(countries: dict, new_country: str, new_state: dict) -> None:
    countries[new_country] = new_state

def get_cities_population(country:str, state:str) -> list:
    countries = {
        "USA": {
            "California": {
                "Los Angeles": 4000000,
                "San Francisco": 870000
            }
        },
        "Canada": {
            "Ontario": {
                "Toronto": 2930000,
                "Ottawa": 994837
            }
        }
    }

    new_country = "Nigeria"
    new_state = {
        "Lagos": {
            "Mainland": 4_200_329,
            "Ikorodu": 4_230_000
        }
    }
    update_country(countries, new_country, new_state)
    try:
        states = countries[country]
    except KeyError:
        return [f"Error: Country {country} not found."]
    try:
        cities = states[state]
    except KeyError:
        return [f"Error: State {state} not in {country}."]

    result = []
    for city, population in cities.items():
        result.append(f"The population of {city} is {population}.")

    return result

