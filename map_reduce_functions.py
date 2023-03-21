def mapper(data):
    return data, 1


def reduce(key, values: list):
    return key, sum(values)
