def print_result(func):
    def new_func(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return new_func

def add_two_ints(a: int, b: int):
    return a + b


if __name__ == "__main__":
    add_two_ints = print_result(add_two_ints)
    add_two_ints(3, 5)


