import math

def determine_number_of_pack(no_of_guest:int, slice_per_pack:int) -> int:
    return math.ceil(no_of_guest/slice_per_pack)
    
def get_index_of_pizza_type(pizza_types:list, pizza_type:str) -> int:
    index = 0
    while index < len(pizza_types):
        if pizza_types[index].lower() == pizza_type.lower():
            return index
        index += 1
    return -1
    
def prepare_output(pizza_type:str, slice_per_pack:int, number_of_box:int, price_per_pack:float, no_of_guest:int) -> str:
    total_slices = slice_per_pack * number_of_box
    total_price = price_per_pack * number_of_box
    remaining_slice = total_slices - no_of_guest

    number_of_box_text = str(number_of_box) + " boxes" if number_of_box > 1 else " box"
    number_of_guest_text = str(no_of_guest) + " persons" if no_of_guest > 1 else " person"
    remaining_slice_text = str(remaining_slice) + " slices" if remaining_slice > 1 else " slice"
    slices_served_text = str(no_of_guest) + " slices" if no_of_guest > 1 else " slice"

    output = f"\n>>> Number of boxes of pizza to buy = {number_of_box_text} "
    output += f"\n(explaination: {pizza_type} size contains {slice_per_pack} slices per box, {number_of_box_text} should be sufficient for {number_of_guest_text} as it would contain {total_slices} slices in all)\n"
    output += f"\n>>> Number left over slices after serving = {remaining_slice_text} \n(explanation: After serving {slices_served_text}, you should have {remaining_slice_text} left)\n"
    output += f"\n>>> Price = {total_price:>.2f} \n(explanation: {price_per_pack:>.2f} per box for {number_of_box_text})\n"
    return output
  
def generate_pizza_menu(pizza_types:list, no_of_slices:list, prices_per_box:list):
    message = "\033[33m\033[1m\t\tIya Moses Pizza joint Ajegunle\n"
    message += f"| {'Pizza type':>15} | {'Number of Slices':>16} | {'Price per box':>15} |\n"
    message += f"+ {('-'*15):>15} + {('-'*15):>16} + {('-'*15):>15} +\n"

    index = 0
    while index < len(pizza_types):
        message += f"| {pizza_types[index]:>15} | {no_of_slices[index]:>15} | {prices_per_box[index]:>15.2f} |\n"
        message += f"+ {('-'*15):>15} + {('-'*15):>16} + {('-'*15):>15} +\n"
        index += 1
    return message + "\033[0m"
	

pizza_types = ["Sapa size", "Small Money", "Big boys", "Odogwu"]
no_of_slices = [4, 6, 8, 12]
prices_per_box = [2500, 2900, 4000, 5200]
pizza_type_index = -1
no_of_guest = 0
pizza_type = ""
print("\033[2J")

while pizza_type_index == -1:
    print(generate_pizza_menu(pizza_types, no_of_slices, prices_per_box))
    
    no_of_guest = int(input("Enter the number of guest: "))

    pizza_type = input("Enter the type of pizza: ")
    pizza_type_index = get_index_of_pizza_type(pizza_types, pizza_type)
    if pizza_type_index == -1:
        print("\033[2J\033[31mWrong input: select pizza type from menu and guests number must be at least 1, try Again\033[0m")
    
slice_per_pack = no_of_slices[pizza_type_index]
price_per_pack = prices_per_box[pizza_type_index]
number_of_box = determine_number_of_pack(no_of_guest, slice_per_pack)
output = prepare_output(pizza_type, slice_per_pack, number_of_box, price_per_pack, no_of_guest)
print(output)

