from datetime import datetime

new_laptop = True
class Shop:
    def __init__(self, laptop_dict_list, laptop_detail_list, laptop_details):
        self.laptop_dict_list = laptop_dict_list
        self.laptop_detail_list = laptop_detail_list
        self.laptop_details = laptop_details
        self.order_laptop()
        

    def order_laptop(self):
        print("Enter the details of the laptop to be ordered : ")
        purchased_date_time = f"{datetime.today().hour}:{datetime.today().minute} {datetime.today().month}/{datetime.today().day}/{datetime.today().year}"
        laptop_name = input("Laptop Name : ").strip()
        laptop_brand = input("Laptop Brand : ").strip()
        global new_laptop

        for laptop in self.laptop_details:
            if laptop_name == laptop[0] and f" {laptop_brand}" == laptop[1]:
                new_laptop = False
                break
        try:
            laptop_quantity = int(input("Laptop Quantity : "))
            laptop_price = int(input("Laptop Price : "))
        except ValueError:
            print("\nEnter the amount in number\nOther Characters aren't allowed\n")
            return
        distributor_name = input("Distributor Name : ")
        shipping_address = input("Shipping Address : ")
        shop_name = "Laptop Shop"
        shop_email = input("Shop Email : ")
        shop_phone = input("Shop Phone : ")

        total_amount_without_vat = laptop_price * laptop_quantity
        vat_amount = 0.13 * total_amount_without_vat
        gross_amount = total_amount_without_vat + vat_amount

        if new_laptop:
            laptop_processor = input("Laptop Processor : ")
            laptop_graphics = input("Laptop Graphics : ")

            for laptop in self.laptop_details:
                with open("laptops.txt", "a") as new_entry:
                    new_entry.write(
                        f"{laptop_name}, {laptop_brand}, {laptop_price}, {laptop_quantity}, {laptop_processor}, {laptop_graphics}\n")
                    break
            print("\nThe purchase is successull..\nPlease Check your invoce for the details\n")
        else:
            with open("laptops.txt", "w") as clear_file:
                clear_file.write("")

            for laptop in self.laptop_details:
                with open("laptops.txt", "a") as laptop_file:
                    if laptop_name == laptop[0] and f" {laptop_brand}" == laptop[1]:
                        price = laptop[2]
                        qty = int(laptop[3]) + laptop_quantity
                        processor = laptop[4]
                        graphics = laptop[5]
                        new_laptop = False
                        laptop_file.write(f"{laptop_name}, {laptop_brand},{price}, {qty},{processor},{graphics}\n")
                    else:
                        laptop_file.write(f"{laptop[0]},{laptop[1]},{laptop[2]},{laptop[3]},{laptop[4]},{laptop[5]}\n")

        self.invoice_generator(purchased_date_time, distributor_name, shop_name, shipping_address, shop_email,
                               shop_phone, total_amount_without_vat, vat_amount, gross_amount, laptop_brand,
                               laptop_name, laptop_quantity, laptop_price)
        print("\nThe purchase is successful\nPlease check your invoce for all the detials.")
        return

    def invoice_generator(self, purchased_date, distributor_name, shop_name, shipping_address, shop_email, shop_phone,
                          bill_amount_without_vat, vat_amount, gross_amount, laptop_brand, laptop_name,
                          laptop_quantity, laptop_price):
        with open(f"{laptop_brand}_{laptop_name}_purchase.txt", "a") as invoice_new:
            with open(f"{laptop_brand}_{laptop_name}_purchase.txt", "w") as clear:
                clear.write("")
            invoice_new.write(purchased_date)
            invoice_new.write("\n\n{:30s} {:30s}".format(f"BILL TO", "SHIP TO"))
            invoice_new.write("\n{:30s} {:30s}".format("_______", "_______"))
            invoice_new.write(
                "\n{:30s} {:30s}\n{:30s} {:30s}\n{:30s} {:30s}".format(shop_name, shop_name, shipping_address,
                                                                       shipping_address, shop_email,
                                                                       shop_phone))
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
                                                                          f'${bill_amount_without_vat}',
                                                                          "|"))
            for i in range(7):
                invoice_new.write("\n{:32s} {:32s} {:32s} {:32s} {:30s}".format('|', '|', '|', '|', "|"))
            invoice_new.write(
                "\n| __________________________________________________________________________________________________________________________________|")
            invoice_new.write("\n{:>67s} {:>30s} | {:^30s} |".format("|", "Shipping Cost", f"${vat_amount}"))
            invoice_new.write(
                "\n{:>133}".format("|_________________________________________________________________|"))
            invoice_new.write("\n{:>67s} {:>30s} | {:^30s} |".format("|", "Total Amount", f"${gross_amount}"))
            invoice_new.write(
                "\n{:>133}".format("|_________________________________________________________________|"))
