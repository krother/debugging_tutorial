
    
def get_partitions(data, granularity):
    """Produces #granularity subsets with left out slices from data"""
    size = max(1, len(data) / granularity)
    start = 0
    while start < len(data):
        end = start + size
        yield data[:int(start)] + data[int(end):]
        start = end


def delta_debug(data, test, granularity=2):
    print('\nexamining "{1}" (granularity={0})'.format(granularity, data))
    for subset in get_partitions(data, granularity):
        result = test(subset)
        print('{} -> {}'.format(subset, result))
        if result == 'FAIL':
            if len(subset) > 1:
                return delta_debug(subset, test, granularity)
            else:
                return subset # minimal failing subset
    if granularity < len(data):
        return delta_debug(data, test, granularity + 1)
    return data

