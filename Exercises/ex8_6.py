def city_country(city_name, country, population=''):
    if population:
        info = f"{city_name.title()}, {country.title()}-population {population}"
    else:
        info = f"{city_name.title()}, {country.title()}"
    return info

city = city_country('Santiago', 'Chile')
print(city)
city = city_country('Guangzhou', 'China')
print(city)
city = city_country('Shanghai', 'China')
print(city)