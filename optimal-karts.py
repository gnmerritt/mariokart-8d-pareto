import sys
from csv import DictReader
import itertools

def read_data(files):
    data = {}
    for f in files:
        rows = []
        filename = f"data/{f}.csv"
        with open(filename, mode='r') as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                rows.append(row)
        data[f] = rows
    return data


def dominated_by(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return False
    return True


def find_optimal(files, attributes):
    print(f"Optimizing {attributes} using {files}")
    data = read_data(files)

    possible = []

    rows_list = [rows for _, rows in data.items()]
    for setup in itertools.product(*rows_list):
        name = tuple(r.get('name') for r in setup)
        stats = {}
        for attr in attributes:
            for r in setup:
                stats[attr] = stats.get(attr, 0) + int(r.get(attr))
        stats = tuple(stats.get(a) for a in attributes)
        possible.append((stats, name))

    possible.sort(reverse=True)
    efficient = []
    current_best = None

    for stats, name in possible:
        if current_best is None or not dominated_by(stats, current_best):
            efficient.append((name, stats))
            current_best = stats

    print(f"Got efficient possibilities")
    width = 40
    for name, stats in efficient:
        name = " - ".join(name)
        print(f"  {name: <60} {stats}")


if __name__ == "__main__":
    data = ['characters', 'karts', 'wheels', 'gliders']
    presets = {
        'prix': ['SL', 'AC', 'TL'],
        'timed': ['SL', 'MT', 'TL'],
    }
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        if not arg in presets.keys():
            print(f"Unrecogized preset '{arg}', available options are {presets}")
            sys.exit(1)
    else:
        arg = 'prix'
    attributes = presets[arg]
    find_optimal(data, attributes)
