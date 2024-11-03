#exercise 3.27 (World Population Growth)
EXTIMATED_POPULATION_NOV_2024 = 8185721163
YEARLY_POPULATION_GROWTH_RATE_2024 = 0.087
YEAR = 2024

print(f'{"year":<5}\t{"population":<12}\t{"increase":<12}')
population = EXTIMATED_POPULATION_NOV_2024
year_doubled = 0
year_quadruple = 0
counter = 1
increase = 0


while True:
    if counter <= 100:
        print(f"{counter:<5}\t{population:<12}\t{increase:<12}")
    else:
        break

    if year_doubled == 0 and (population // 2) >= EXTIMATED_POPULATION_NOV_2024:
        year_doubled = YEAR + counter
        visited = True
    elif year_quadruple == 0 and (population // 4) >= EXTIMATED_POPULATION_NOV_2024:
        year_quadruple = YEAR + counter
        if counter > 100:
            break
    growth = int(population * YEARLY_POPULATION_GROWTH_RATE_2024)
    population += growth
    increase = population - EXTIMATED_POPULATION_NOV_2024
    counter += 1

print(f"Current population ({EXTIMATED_POPULATION_NOV_2024}) doubled and quadrupled in year {year_doubled} and {year_quadruple} respectively.  ")


