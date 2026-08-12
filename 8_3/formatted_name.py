def get_formmatted_name(first_name, last_name, middle_name=None):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formmatted_name('jimi', 'hendrix')
print(musician)

musician = get_formmatted_name('john', 'lee', 'hooker')
print(musician)