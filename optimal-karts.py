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


def dominates(a, b):
    for i in range(len(a)):
        if a[i] <= b[i]:
            return False
    return True


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
    for p in efficient:
        print(f"  {p}")


if __name__ == "__main__":
    # just optimize acceleration & speed for now as proof-of-concept
    data = ['characters', 'karts', 'wheels', 'gliders']
    attributes = ['SL', 'AC']
    find_optimal(data, attributes)
