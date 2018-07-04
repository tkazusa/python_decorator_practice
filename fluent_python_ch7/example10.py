"""
Fluent Python Ch.7 example11
"""


def make_averager():
    count = 0
    total = 0
    
    def averager(new_value):
        count += 1  # reassignment
        total += new_value # reassignment
        return total / count

    return averager

if __name__ == "__main__":
    avg = make_average()
    print(avg(10))
    print(avg(11))
    print(avg(12))

