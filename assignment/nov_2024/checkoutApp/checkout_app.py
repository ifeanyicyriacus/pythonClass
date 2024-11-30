from datetime import datetime

def add_purchases_to_list(product_name_list:list, product_qty_price_and_total_list:list) -> None:
    isShopping = True
    while(isShopping):
        product_name = input("Enter product purchased: ")
        product_name_list.append(product_name)
        units_purchased = float(input("Enter number of unit purchased: "))
        price_per_unit = float(input("Enter price per unit: NGN "))
        product_qty_price_and_total_list.append([units_purchased, price_per_unit, (units_purchased * price_per_unit)])
        isShopping = input("Want to add more Items (yes/no)? ").lower() == "yes"
    
def display_invoice(message:str, cashier_name:str, customer_name:str, product_names_list:list, product_qty_price_and_total_list:list, sub_total:float, discount:float, vat_applied:float, bill_total:float) -> str:
    dashes_equal = "=" * 50 +"\n"
    dashes_minus = "-" * 50 +"\n"
    date = str(datetime.now())[:19]
    
    message += f"Date: {date}\n"
    message += f"Cashier: = {cashier_name}\n"
    message += f"Customer Name:{customer_name}\n"
    message += dashes_equal
    message += f"{'ITEM':>15}\t{'QTY':>5}\t{'PRICE':>7}\t{'TOTAL(NGN)':>13}\n" 
    message += dashes_minus
    message += display_items(product_name_list, product_qty_price_and_total_list)
    message += dashes_minus
    message += f"\t\t{'Sub Total:':>15}\t{sub_total:>13.2f}\n"
    message += f"\t\t{'Discount:':>15}\t{discount:>13.2f}\n"
    message += f"\t\t{'VAT @ 7.5%:':>15}\t{vat_applied:>13.2f}\n"
    message += dashes_equal
    message += f"\t\t{'Bill Total:':>15}\t{bill_total:>13.2f}\n"
    return message
    
def display_items(product_name_list:list, product_qty_price_and_total_list:list) -> str:
    items = ""
    for index in range(len(product_name_list)):
        items += f"{product_name_list[index]:>15}\t"
        items += f"{product_qty_price_and_total_list[index][0]:>5.1f}\t"
        items += f"{product_qty_price_and_total_list[index][1]:>7.2f}\t" 
        items += f"{product_qty_price_and_total_list[index][2]:>13.2f}\n"
    return items + "\n"


def calculate_sub_total(product_qty_price_and_total_list:list) -> float:
    return sum([item[2] for item in product_qty_price_and_total_list])

def display_payment_summary(bill_total:float, payment:float) -> str:
    message = f"\t\t{'Amount Paid:':>15}\t{payment:>13.2f}\n"
    message += f"\t\t{'Balance:':>15}\t{(payment - bill_total):>13.2f}\n"
    return message
    
VAT = 0.075
product_name_list = []
product_qty_price_and_total_list = []
client_header = """
\033[1m
SEMICOLON STORES
(HEAD OFFICE)
LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.
TEL: 03293828343
\033[0m"""

print(client_header)
customer_name = input("What is the customer name? ")
add_purchases_to_list(product_name_list, product_qty_price_and_total_list)
cashier_name = input("Enter you name to sign off: ")
discount_rate = float(input("Enter discount rate: ")) / 100

sub_total = calculate_sub_total(product_qty_price_and_total_list)
discount = sub_total * discount_rate
vat_applied = sub_total * VAT
bill_total = sub_total - discount + vat_applied

print(display_invoice(client_header, cashier_name, customer_name, product_name_list, product_qty_price_and_total_list, sub_total, discount, vat_applied, bill_total))
print("=" * 50)
print(f"THIS IS NOT A RECEIPT KINDLY PAY {bill_total:>12.2f}");
print("=" * 50)
payment = float(input("How much did the customer give you?"));

print(display_invoice(client_header, cashier_name, customer_name, product_name_list, product_qty_price_and_total_list, sub_total, discount, vat_applied, bill_total))
print(display_payment_summary(bill_total, payment))
print("=" * 50)
print("\t\tTHANK YOU FOR YOUR PATRONAGE")
print("=" * 50)



