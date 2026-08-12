favourite_places = {
    'a': ['french', 'england'],
    'b': ['spain'],
    'c': ['argentina', 'egypt', 'norway'],
}
for name, places in favourite_places.items():
    print(f"{name.title()}:")
    for place in places:
        print(f"{place.title()}")