"""
Fluent Python Ch.7 example5
"""


def f3(a):
    global b
    print(a)
    print(b)
    b = 9


if __name__ == "__main__":
    b = 6
    f3(3)
