"""
Fluent Python Ch.7 example1
"""

def deco(func):
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target')


if __name__ == "__main__":
    # example 7-1
    print(target())
    print(target)
