
def remove_from_cart(cart:list)-> None:
    product = input("Enter the product you want to remove: ")
    index = 0
    cart_index = None
    while index < len(cart):
        if cart[index][0].lower() == product.lower():
            cart_index = index
            break
        index += 1
    if not (cart_index == None):
        success_message = cart[cart_index][0] + " has been removed to your cart.\n"
        cart.remove(cart[cart_index])
        print(success_message)
    else:
        print(product +" is not on your cart.\n")

def add_to_cart(cart:list, products:list) -> None:
    product = input("Enter the product you want to add: ")    
    index = 0
    product_index = None
    while index < len(products):
        if products[index][0].lower() == product.lower():
            product_index = index
            break
        index += 1
    if product_index == None:
        print(product + " is not a valid product name, Enter (1) to view product list. Try again.\n")
    else:
        cart.append(products[product_index])
        success_message = products[product_index][0] + " has been added from your cart.\n"
        print(success_message)
    

def view_products(products:list) -> None:
    index = 0
    while index < len(products):
        product = products[index][0]
        price =  products[index][1]
        print(f"{index + 1}. {product} - ${price}")
        index += 1
    print()
    
def view_cart(cart:list) -> None:
    if len(cart) == 0:
        print("Your cart is currently empty.\n")
    else:
        index = 0
        while index < len(cart):
            product = cart[index][0]
            price =  cart[index][1]
            print(f"{index + 1}. {product} - ${price}")
            index += 1
    print()
    
def calculate_total(cart:list) -> float:
    return sum([product[1] for product in cart])


def checkout(cart) -> None:
    total = calculate_total(cart)
    print(f"Thank you for shopping with us! Your total is ${total}\n")
    cart.clear()
    
    
    
products = [["Laptop", 1000], ["Phone", 500], ["Headphones", 100]]
cart = []
shopping = True
main_menu = """Welcome to Jessica's E-Store!
1. View Products
2. Add to Cart
3. Remove from Cart
4. View Cart
5. Checkout
6. Exit

Enter menu number >>> """

while(shopping):
    try:
        value = int(input(main_menu))  
        match value:
            case 1:
                view_products(products)
            case 2:
                add_to_cart(cart, products)
            case 3:
                remove_from_cart(cart)
            case 4:
                view_cart(cart)
            case 5:
                checkout(cart)
            case 6:
                shopping = not shopping
    except ValueError:
        print("Enter a valid menu number\n")


