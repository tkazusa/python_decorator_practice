"""
Fluent Python Ch.7
"""

#
# example 7-1
#

def deco(func):
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target')

#
# example 7-2
#

registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')


@register
def f3():
    print('running f3()')

def main():
    print('running main()')
    print('register ^>', registry)
    f1()
    f2()
    f3()


#
# example 7-3
#



if __name__ == "__main__":
    # example 7-1
    print(target())
    print(target)
    
    # example 7-2
    main()
