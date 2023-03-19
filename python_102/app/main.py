import utils
import read_csv as r
import charts


def run():
    data = r.read_csv('data.csv')

    country = input('Enter a country: ')

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)


if __name__ == '__main__':
    run()
