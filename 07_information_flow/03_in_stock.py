def fruit_stock(fruit):
    if fruit == 'apple':
        return 2
    if fruit == 'papaya':
        return 2
    if fruit == 'pineapple':
        return 2
    if fruit == 'banana':
        return 2
    else:
        return 0
    
def main():
    fruit = input("Enter a fruit name :")
    stock = fruit_stock(fruit)
    if stock == 0:
        print("Out of stock")
    else:
        print("AVAILABLE in stock.")
        print(stock ,"is available")

if __name__ == '__main__':
    main()