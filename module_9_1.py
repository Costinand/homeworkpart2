def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        res = (func(int_list))
        results[func.__name__] = res
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func([6, 0, 15, 11], str, type))