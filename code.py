prices=[]
while True:
    item= input('Enter the name of the item (p to quit): ')
    if item.lower() == 'p':
        break
    else:
        price = float(input('Enter the price of the item:$ '))
        items.append(item)
        prices.append(price)
        for i in items:
            print('item is', i)
        for p in prices:
            print('price is $', p)
        total = sum(prices)
        print(f'the total cost is $ {total}')

