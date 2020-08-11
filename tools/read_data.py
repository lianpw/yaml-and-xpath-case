import yaml


def read_data(filename):
    filepath = './data/' + filename
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.load(f)


if __name__ == '__main__':
    data = read_data('search_data.yml')
    print(data)