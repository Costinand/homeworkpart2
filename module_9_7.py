
def is_prime(func):
    def check_func(*args):

        result = func(*args)

        for i in range(3, int(result ** 0.5) + 1, 2):
            if result % i == 0 or result % 2 == 0:
                res = "Составное"
            else:
                res = "Простое"
            print(res)
        return result
    return check_func

@is_prime
def sum_three(*numbers):
    result = sum(numbers)
    return result

result = sum_three(2, 3, 6)
print(result)
