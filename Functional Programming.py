fruits = ['mango', 'banana', 'guava', 'apple', 'grapes', 'watermelon', 'kiwi']
basket = iter(fruits)

print(next(basket))
print(next(basket))
print(next(basket))


def sqare(limit):
    x = 0
    while x< limit:
        yield x*x
        yield x*x*x
        x += 1

a = sqare(5)
print(next(a), next(a))
print(next(a), next(a))
print(next(a), next(a))