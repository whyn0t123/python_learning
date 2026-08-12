cities = {
    'guangzhou': {
        'country': 'china',
        'population': '19million',
        'fact': ['food', 'flower'],
    },
    'new york': {
        'country': 'america',
        'population': '8.5million',
        'fact': ['luxury'],
    },
    'paris': {
        'country': 'french',
        'population': '2.1million',
        'fact': ['sadness'],
    }
}

for city, info in cities.items():
    print(f"{city.title()}:")
    country = info['country']
    population = info['population']
    facts = info['fact']
    print(f"{country}")
    print(f"{population}")
    print("Fact(s):")
    for fact in facts:
        print(f"{fact}\n")