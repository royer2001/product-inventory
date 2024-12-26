from itertools import product

from Product import Product, ProductException


class Inventory:
    def __init__(self):
        self.products_dict = {}
        self.next_account_number = 0

    def validate_key(self, key):
        try:
            key = int(key)
        except ValueError:
            raise ProductException('The value must be an Integer')
        if key not in self.products_dict:
            raise ProductException(f'There is no product with id {key}')
        return key

    def create_product(self, name, price, stock):
        o_product = Product(name, price, stock)
        new_product_number = self.next_account_number
        self.products_dict[new_product_number] = o_product
        self.next_account_number = self.next_account_number + 1
        return new_product_number

    def add_product(self):
        print('Add'.center(10,'*'))
        product_name = input('Enter name: ')
        product_price = input('Enter price: ')
        product_stock = input('Enter stock: ')
        self.create_product(product_name, product_price, product_stock)

    def edit_product(self):
        print('Edit'.center(10,'*'))
        key = input('Enter id to edit: ')
        key = self.validate_key(key)
        name = input('Enter new name: ')
        price = input('Enter new price: ')
        stock = input('Enter new stock: ')
        self.products_dict[key] = Product(name, price, stock)

    def delete_product(self):
        print('Delete'.center(10,'*'))
        key = input('Enter id to delete: ')
        key = self.validate_key(key)
        del self.products_dict[key]
        print('Product deleted successfully')

    # List products with format
    def show_list(self):
        for key in self.products_dict:
            o_product = self.products_dict[key]
            product_key = str(key).ljust(5)
            product_name = str(o_product.name).ljust(15)
            product_price = str(o_product.price).ljust(15)
            product_stock = str(o_product.stock).ljust(5)
            print(f"{product_key} {product_name} {product_price} {product_stock}")