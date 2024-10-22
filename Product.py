class ProductException(Exception):
    """Handle errors for product"""
    pass


class Product:
    def __init__(self, name, price, stock):
        self.name = self.validate_name(name)
        self.price = self.validate_price(price)
        self.stock = self.validate_stock(stock)

    @staticmethod
    def validate_name(name):
        if not name or name.strip() == "":
            raise ProductException('Product name cannot be empty')
        return name

    @staticmethod
    def validate_price(price):
        try:
            price = float(price)
        except ValueError:
            raise ProductException('Price must be a Float')
        return price

    @staticmethod
    def validate_stock(stock):
        try:
            stock = int(stock)
        except ValueError:
            raise ProductException('Stock must be a Integer')
        if stock <= 0:
            raise ProductException('Stock must be a positive number')
        return stock

