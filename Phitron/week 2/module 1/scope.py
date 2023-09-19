balance = 500

def cost(price, quantity):
    global balance
    total = price * quantity
    
    balance = balance - total
    return balance


print(cost(10, 5))