def make_car(maker, type, **info):
    info['maker'] = maker
    info['type'] = type
    return info

car = make_car('sabaru', 'outback', color='blue', two_package=True)
print(car)