import utils
import read_csv as r
import charts


def run():
    data = r.read_csv('data.csv')

    # Solución de compañero
    # percentages_dict = {item["Country/Territory"]: item["World Population Percentage"] for item in data}
    # labels = percentages_dict.keys()
    # values = percentages_dict.values()

    # Solución mia
    # labels = list(map(lambda item: item['Country/Territory'], data))
    # values = list(map(lambda item: item['World Population Percentage'], data))

    # Solución GitHub Copilot
    labels, values = zip(*[(item['Country/Territory'], item['World Population Percentage']) for item in data])
    charts.generate_pie_chart(labels, values)


if __name__ == '__main__':
    run()
