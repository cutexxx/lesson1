studentIds = {'knuth': 42.0, 'turing': 56.0, 'nash': 92.0}
print(studentIds['turing'])

studentIds['nash'] = 'ninety-two'
print(studentIds)

del studentIds['knuth']
print(studentIds)

studentIds['knuth'] = [42.0, 'forty-two']
print(studentIds)

print(studentIds.keys())

print(studentIds.values())
print(studentIds.items())
print(len(studentIds))


fruits = ['apples', 'oranges', 'pears', 'bananas']
for fruit in fruits:
    print(fruit + ' for sale')

fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75}
for fruit, price in fruitPrices.items():
    if price < 2.00:
        print('%s cost %f a pound' % (fruit, price))
    else:
        print(fruit + ' are too expensive!')
