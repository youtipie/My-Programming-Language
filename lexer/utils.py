import tabulate


def print_table(data):
    if data:
        header = data[0].keys()
        rows = [x.values() for x in data]
        print(tabulate.tabulate(rows, header))
    else:
        print([])
