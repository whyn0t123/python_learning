def describe_city(city_name, country='china'):
    print(f"{city_name.title()} is in {country.title()}.")

describe_city('guangzhou')
describe_city('paris', 'french')
describe_city('london', 'england')