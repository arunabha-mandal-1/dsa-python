# Arrays in linked list

stock_prices=[298,305,320,301,292]
# in python, memory representation is little bit different cuz python uses arrays and objects
# in python, list is implemented a dynamic array
# python can store integer and text both in the same array

# lookup by index => O(1)
print(stock_prices[2])

# lookup by value => O(n)
value=301
for i in range(len(stock_prices)):
    if stock_prices[i]==value:
        print(str(value)+" at index "+str(i))

# array traversal => O(n)
for price in stock_prices:
    print(price)

# insert at an index=> O(n)
# cuz next elements have to move one index ahead
stock_prices.insert(1,200)
print(stock_prices)

# delete at an index=> O(n) 
# stock_prices.remove(200) # removes first occurance of the specific element using value
stock_prices.pop(1) # using index the specific element will be removed otherwise the last element will be removed
print(stock_prices)