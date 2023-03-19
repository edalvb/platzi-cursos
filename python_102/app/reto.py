import csv
from charts import generate_bar_chart


def get_keys_anios(header):
    keys = []
    for i in range(1, len(header)):
        if header[i].find('Population') != -1 and \
                get_anio(header[i]) is not None:
            keys.append(header[i])
    return keys


def get_anio(key):
    spl = key.split(' ')
    if len(spl) > 0 and spl[0].isdigit():
        return int(spl[0])
    return None


def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')

        header = next(reader)
        data = []
        # print(header)

        keys_anios = get_keys_anios(header)

        print("keys_anios", keys_anios)

        for row in reader:
            iter = zip(header, row)
            country_dic = {k: v for k, v in iter}

            dict_anio = {}

            for key in keys_anios:
                anio = get_anio(key)

                if anio is not None:
                    dict_anio[str(anio)] = country_dic[key]

            country_dic['pop_anio'] = dict_anio

            data.append(country_dic)

            # print(country_dic)

        country = 'Peru'
        regs = [x for x in data if x['Country/Territory'] == country]

        if len(regs) > 0:
            country_data = regs[0]
            labels = list(country_data['pop_anio'].keys())
            values = list(country_data['pop_anio'].values())

            print('labels', labels)
            print('values', values)

            generate_bar_chart(labels, values)

            # print(country_data)
        else:
            print('No se encontró el país')

        return data


if __name__ == '__main__':
    read_csv('./data.csv')
