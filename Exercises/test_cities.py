from ex8_6 import city_country

def test_city_country():
    city = city_country('santiago', 'chile', population=5000000)
    assert city == 'Santiago, Chile-population 5000000'