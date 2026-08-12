favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")

for name in favourite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
        
if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")
#6.3.3
for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
#6.3.4
print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())

people = ['jen', 'sarah', 'mike', 'anna']
for person in people:
    if person in favourite_languages.keys():
        print(f"Thank you for taking the poll, {person}!")
    else:
        print(f"Welcome to taking the poll, {person}!")