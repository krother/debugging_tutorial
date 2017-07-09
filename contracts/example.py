
from covenant import pre, post

    
@pre(lambda number: number >= 1)
@post(lambda result, number: len(result) == number)
def square_numbers(number):
    result = []
    for i in range(1, number+1):
        result.append(i ** 2)


if __name__ == '__main__':
    print(square_numbers(3))
    print(square_numbers(-1))
    