# Shoping-cart---python
A beginner Python shopping cart program.

Features:
1-Add multiple items
2- Store prices using lists
3- Calculate total cost
4- Display a receipt

Skills used:
1- Loops
2- Lists
3- User input
4- Functions like sum()

CODE:
items= []
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
            print('price is $',p)
        total= sum(prices)
        print(f'the total cost is $ {total}')
