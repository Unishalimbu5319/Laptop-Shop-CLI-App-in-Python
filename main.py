from customer import Customer
from shop import Shop



is_shop_closed = False

while not is_shop_closed:
    laptop_dict_list = []
    sn = 1
    with open("laptops.txt") as laptop_list:
        laptop_details = [line.strip().split(",") for line in laptop_list]
        laptop_detail_list = laptop_details
        # print(laptop_detail_list)
        # print(laptop_details)
        for detail in laptop_details:
            laptop_dict = {
                "id": sn,
                "laptop_name": detail[0],
                "laptop_brand": detail[1],
                "laptop_price": detail[2],
                "laptop_quantity": detail[3],
                "laptop_processor": detail[4],
                "laptop_graphics": detail[5]
            }
            laptop_dict_list.append(laptop_dict)
            sn += 1
    try:
        user_input = int(input("Who are you?\nEnter 1 for Customer\nEnter 2 for Admin\nEnter 0 to exit\n-> "))
    except ValueError:
        print("Only numbers are allowed, pleae enter a number!!")
        continue
    
    if user_input == 1:
        customer = Customer(laptop_dict_list, laptop_detail_list, laptop_details)
    elif user_input == 2:
        shop = Shop(laptop_dict_list, laptop_detail_list, laptop_details)
    elif user_input == 0:
        is_shop_closed = True
    else:
        print("Invalid Serial Number\nCheck the list and input a valid one")


