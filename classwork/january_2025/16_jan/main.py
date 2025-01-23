from country import get_cities_population

print("Welcome to iFinder Services")
print("City Population Finder")
country_name = input("Enter the name of a country: ")
state_name = input("Enter the state or province: ")

cities = get_cities_population(country_name, state_name)
for city in cities:
    print(f"\033[31m{city}")