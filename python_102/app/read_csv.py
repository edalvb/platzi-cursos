import csv


def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')

        header = next(reader)
        data = []
        # print(header)

        for row in reader:
            iter = zip(header, row)
            country_dic = {k: v for k, v in iter}

            data.append(country_dic)
            # print(country_dic)
        return data


if __name__ == '__main__':
    read_csv('./data.csv')
