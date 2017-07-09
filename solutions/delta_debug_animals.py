"""
Sample solution to the Delta Debugging exercise
"""

from ddebug import delta_debug

class AnimalError(Exception): pass

def print_animals(names):
    """Prints animals but only if they get along well"""
    if 'cat' in names and 'dog' in names: raise(AnimalError())
    if 'wolf' in names and 'pig' in names: raise(AnimalError())
    if 'anteater' in names and 'ant' in names: raise(AnimalError())
    print(';'.join(names))


def test_animals(names):
    try:
        print_animals(names)
        return 'PASS'
    except AnimalError:
        return 'FAIL'


if __name__ == '__main__':
    data = ['pig', 'chicken', 'dog', 'anteater', 'wolf', 'piranha']
    result = delta_debug(data, test_animals)
    print("minimal failing set: ", result)
