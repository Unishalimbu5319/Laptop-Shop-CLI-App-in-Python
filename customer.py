from datetime import datetime

class Customer:
    def __init__(self, laptop_dict_list, laptop_detail_list, laptop_details):
        self.laptop_detail_list = laptop_detail_list
        self.laptop_dict_list = laptop_dict_list
        self.laptop_details = laptop_details
        self.menu_display(item_list=laptop_dict_list)
        self.buy(laptop_dict_list)


    def menu_display(self, item_list):
        print("---------------------- Laptop Shop ---------------------")
        print("Here are all the laptops in our stock")
        print("{:4s} {:20s} {:20s} {:20s} {:20s} {:20s} {:20s}".format("S.N", "Name", "Brand", "Price", "Quantity",
                                                                       "Processor", "Graphics"))
        for item in item_list:
            print("{:3d} {:20s} {:20s} {:20s} {:20s} {:20s} {:20s}".format(item["id"], item["laptop_name"],
                                                                           item["laptop_brand"], item["laptop_price"],
                                                                           item["laptop_quantity"],
                                                                           item["laptop_processor"],
                                                                           item["laptop_graphics"]))

    def buy(self, laptops_list):
        try:
            serial_num = int(input("Enter the serial number of the laptop you want to buy from the above list : "))
        except ValueError:
            print("Enter a valid input")
            return
        is_in_list = False
        for d in laptops_list:
            if d["id"] == serial_num:
                is_in_list = True
                dt = datetime.today()
                purchased_date = f"{dt.month}/{dt.day}/{dt.year}"
                user_name = input("Enter your name : ")
                try:                    
                    quantity = int(input("Enter the number of laptops to purchase : "))
                    if quantity > int(d["laptop_quantity"]):
                        print(f'\nWe don\'t have enough stock to match your requirements.\n{d["laptop_quantity"]} laptops are there\n')
                        break
                except ValueError:
                    print("\nEnter a valid amount, not alphabets\n")
                    break
                bill_amount_without_shipping_cost = quantity * int(d["laptop_price"].replace("$", ""))
                shipping_cost = 22.65
                total_cost = shipping_cost + bill_amount_without_shipping_cost
                user_email = input("Enter your email : ")
                user_phone = input("Enter you phone number : ")
                shipping_address = input("Enter the shipping address : ")
                laptop_shop = "Laptop Shop"

                self.invoice_generator(purchased_date, laptop_shop, user_name, shipping_address, user_email, user_phone,
                                  bill_amount_without_shipping_cost, shipping_cost, total_cost, d["laptop_brand"],
                                  d["laptop_name"], quantity, d["laptop_price"])
                
                laptop = d["laptop_name"]
                with open("laptops.txt", "r") as data_file:
                    laptop_stock = self.laptop_detail_list[serial_num - 1][3]
                    if int(laptop_stock) > 0:
                        new_laptop_stock = int(laptop_stock) - quantity
                    else:
                        print(
                            "\nCurrently there are no laptops of this model available\nPlease wait for the supplier to restock")
                        exit(0)
                    new_laptop_list = [line.split(",") for line in data_file]
                    new_data_string = ""

                    for element in new_laptop_list:
                        if laptop in element:
                            element.remove(element[3])
                            element.insert(3, f" {new_laptop_stock}")
                        new_data_string += ",".join(element)

                    with open("laptops.txt", "w") as new_data_file:
                        new_data_file.write(new_data_string)
                        print("\nThe purchase is sucessfull, please check your invoice for all the details..\nThank You For Taking Our Service\n")
                        break
        if not is_in_list:
            print("\nEnter a valid serial number\nPlease check again and enter again")

    def invoice_generator(self, purchased_date, laptop_shop, user_name, shipping_address, user_email, user_phone,
                          bill_amount_without_shipping_cost, shipping_cost, total_cost, laptop_brand, laptop_name,
                          laptop_quantity, laptop_price):
        try:
            with open(f"{user_name}.txt", "w") as invoice_new:
                invoice_new.write(purchased_date)
                invoice_new.write("\n{:30}".format(f"{laptop_shop}"))
                invoice_new.write("\n\n{:30s} {:30s}".format(f"BILL TO", "SHIP TO"))
                invoice_new.write("\n{:30s} {:30s}".format("_______", "_______"))
                invoice_new.write(
                    "\n{:30s} {:30s}\n{:30s} {:30s}\n{:30s} {:30s}".format(user_name, user_name, shipping_address,
                                                                           shipping_address, user_email,
                                                                           user_phone))
                invoice_new.write(
                    "\n\n __________________________________________________________________________________________________________________________________")
                invoice_new.write(
                    "\n| {:^30s} | {:^30s} | {:^30s} | {:^30s} |".format("DESCRIPTION", "QTY", "UNIT PRICE", "TOTAL"))
                invoice_new.write(
                    "\n| __________________________________________________________________________________________________________________________________|")
                invoice_new.write(
                    "\n{} {:^30s} {} {:^30s} {} {:^30s} {} {:^30s} {}".format("|", f'{laptop_brand} {laptop_name}',
                                                                              "|", f'{laptop_quantity}', "|",
                                                                              f'{laptop_price}',
                                                                              "|",
                                                                              f'${bill_amount_without_shipping_cost}',
                                                                              "|"))
                for i in range(7):
                    invoice_new.write("\n{:32s} {:32s} {:32s} {:32s} {:30s}".format('|', '|', '|', '|', "|"))
                invoice_new.write(
                    "\n| __________________________________________________________________________________________________________________________________|")
                invoice_new.write("\n{:>67s} {:>30s} | {:^30s} |".format("|", "Shipping Cost", f"${shipping_cost}"))
                invoice_new.write(
                    "\n{:>133}".format("|_________________________________________________________________|"))
                invoice_new.write("\n{:>67s} {:>30s} | {:^30s} |".format("|", "Total Amount", f"${total_cost}"))
                invoice_new.write(
                    "\n{:>133}".format("|_________________________________________________________________|"))
        except FileNotFoundError:
            with open(f"{user_name}.txt", "a") as invoice:
                invoice.write(purchased_date)
                invoice.write("\n\n{:30s} {:30s}".format(f"BILL TO", "SHIP TO"))
                invoice.write("\n{:30s} {:30s}".format("_______", "_______"))
                invoice.write(
                    "\n{:30s} {:30s}\n{:30s} {:30s}\n{:30s} {:30s}".format(user_name, user_name, shipping_address,
                                                                           shipping_address, user_email, user_phone))
                invoice.write(
                    "\n\n __________________________________________________________________________________________________________________________________")
                invoice.write(
                    "\n| {:^30s} | {:^30s} | {:^30s} | {:^30s} |".format("DESCRIPTION", "QTY", "UNIT PRICE", "TOTAL"))
                invoice.write(
                    "\n| __________________________________________________________________________________________________________________________________|")
                invoice.write(
                    "\n{} {:^30s} {} {:^30s} {} {:^30s} {} {:^30s} {}".format("|", f'{laptop_brand} {laptop_name}',
                                                                              "|", f'{laptop_quantity}', "|",
                                                                              f'{laptop_price}',
                                                                              "|",
                                                                              f'${bill_amount_without_shipping_cost}',
                                                                              "|"))
                for i in range(7):
                    invoice.write("\n{:32s} {:32s} {:32s} {:32s} {:30s}".format('|', '|', '|', '|', "|"))
                invoice.write(
                    "\n| __________________________________________________________________________________________________________________________________|")
                invoice.write("\n{:>67s} {:>30s} | {:^30s} |".format("|", "Shipping Cost", f"${shipping_cost}"))
                invoice.write("\n{:>133}".format("|_________________________________________________________________|"))
                invoice.write("\n{:>67s} {:>30s} | {:^30s} |".format("|", "Total Amount", f"${total_cost}"))
                invoice.write("\n{:>133}".format("|_________________________________________________________________|"))
