def get_population(country_dict):
    population_dict = {
        '2022': float(country_dict['2022 Population']),
        '2020': float(country_dict['2020 Population']),
        '2015': float(country_dict['2015 Population']),
        '2010': float(country_dict['2010 Population']),
        '2000': float(country_dict['2000 Population']),
        '1990': float(country_dict['1990 Population']),
        '1980': float(country_dict['1980 Population']),
        '1970': float(country_dict['1970 Population']),
    }

    keys = list(population_dict.keys())
    values = list(population_dict.values())

    return keys, values


def population_by_country(data, country):
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result
