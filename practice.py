def print_result(func):
    """decorator for print result
    Args:
        func: function 
    return:
        new_func:function decorated with printing calclation result
    """
    def new_func(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return new_func

def print_args(func):
    """decorator for print argments
    Args:
        func: function 
    return:
        new_func:function decorated with printing argments used in func
    """
    def new_func(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs)
    return new_func


def print_messages(start_message: str, end_message: str):
    """decoraot for print massages
    Args:
        func: function 
        start_message: start
        end_message: end
    return:
        new_func:function decorated with printing massages
    """
    def _print_messages(func):
        def new_func(*args, **kwargs):
            print(start_message)
            result = func(*args, **kwargs)
            print(end_message)
            return result
        return new_func
    return _print_messages


def add_two_ints(a: int, b: int):
    return a + b

@print_messages('start', 'end')
@print_args
@print_result
def multiple_two_ints(a: int, b: int):
    return a * b


if __name__ == "__main__":
    add_two_ints = print_result(add_two_ints)
    add_two_ints(3, 5)
    multiple_two_ints(3, 5)
