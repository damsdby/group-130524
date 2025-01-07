from peewee import *
from datetime import datetime


db = SqliteDatabase('clothing_store.db')


class Customer(Model):
    """
    Represents a customer in the clothing store database.

    Attributes:
        name (str): The name of the customer
        email (str): The email address of the customer
        phone (str): The phone number of the customer
    """
    name = CharField()
    email = CharField(unique=True)
    phone = CharField()

    class Meta:
        database = db


class Product(Model):
    """
    Represents a product available for sale in the store

    Attributes:
        name (str): The name of the product
        description (str): A brief description of the product
        price (float): The price of the product
        stock (int): The available quantity of the product
        manufacture_date (date): The date the product was manufactured
    """
    name = CharField()
    description = TextField()
    price = FloatField()
    stock = IntegerField()
    manufacture_date = DateField()

    class Meta:
        database = db


class Seller(Model):
    """
    Represents a seller in the store database

    Attributes:
        name (str): The name of the seller
        email (str): The email address of the seller
    """
    name = CharField()
    email = CharField()

    class Meta:
        database = db


class Purchase(Model):
    """
    Represents a purchase made in the store

    Attributes:
        customer: The customer who made the purchase
        product: The product that was purchased
        seller: The seller who sold the product
        quantity: The quantity of the product purchased
    """
    customer = ForeignKeyField(Customer, backref='purchases')
    product = ForeignKeyField(Product, backref='purchases')
    seller = ForeignKeyField(Seller, backref='sales')
    quantity = IntegerField()

    class Meta:
        database = db


db.connect()
db.create_tables([Customer, Product, Seller, Purchase], safe=True)


if Customer.select().count() == 0:
    customers = [
        {'name': 'ogbudda', 'email': 'ogbudda@example.com', 'phone': '+380501234567'},
        {'name': 'kyiv_stoner', 'email': 'kyiv.stoner@example.com', 'phone': '+380671234567'},
        {'name': 'alyona alyona', 'email': 'alyona@example.com', 'phone': '+380631234567'},
        {'name': 'Skofka', 'email': 'skofka@example.com', 'phone': '+380931234567'},
        {'name': 'Kalush', 'email': 'kalush@example.com', 'phone': '+380661234567'}
    ]
    Customer.insert_many(customers).execute()

if Product.select().count() == 0:
    products = [
        {'name': 'Stone Island Hoodie', 'description': 'Premium quality hoodie', 'price': 300.00, 'stock': 15,
         'manufacture_date': datetime(2022, 5, 1).date()},
        {'name': 'Adidas Sneakers', 'description': 'Comfortable running sneakers', 'price': 150.00, 'stock': 40,
         'manufacture_date': datetime(2023, 3, 15).date()},
        {'name': 'Nike T-shirt', 'description': 'Stylish and breathable', 'price': 50.00, 'stock': 100,
         'manufacture_date': datetime(2021, 8, 10).date()},
        {'name': 'Arcteryx Jacket', 'description': 'Waterproof and durable', 'price': 450.00, 'stock': 10,
         'manufacture_date': datetime(2023, 1, 5).date()},
        {'name': 'The North Face Backpack', 'description': 'Spacious and lightweight', 'price': 200.00, 'stock': 30,
         'manufacture_date': datetime(2023, 7, 20).date()}
    ]
    Product.insert_many(products).execute()

if Seller.select().count() == 0:
    sellers = [
        {'name': 'Stone Island', 'email': 'ston@gmail.com'},
        {'name': 'Adidas', 'email': 'adidas@gmail.com'},
        {'name': 'Nike', 'email': 'nike@gmail.com'},
        {'name': 'Arcteryx', 'email': 'arcteryx@gmail.com'},
        {'name': 'The North Face', 'email': 'tnf@gmail.com'}
    ]
    Seller.insert_many(sellers).execute()

if Purchase.select().count() == 0:
    purchases = [
        {'customer': 1, 'product': 1, 'seller': 1, 'quantity': 1},
        {'customer': 2, 'product': 2, 'seller': 2, 'quantity': 2},
        {'customer': 3, 'product': 3, 'seller': 3, 'quantity': 3},
        {'customer': 4, 'product': 4, 'seller': 4, 'quantity': 1},
        {'customer': 5, 'product': 5, 'seller': 5, 'quantity': 2}
    ]
    Purchase.insert_many(purchases).execute()


most_popular = (Product
                .select(Product.name, fn.SUM(Purchase.quantity).alias('total_sales'))
                .join(Purchase)
                .group_by(Product)
                .order_by(fn.SUM(Purchase.quantity).desc())
                .first())
print(f"Most popular product: {most_popular.name}, Total Sales: {most_popular.total_sales}")


most_expensive = Product.select().order_by(Product.price.desc()).first()
print(f"Most expensive product: {most_expensive.name}, Price: {most_expensive.price}")


newest_product = Product.select().order_by(Product.manufacture_date.desc()).first()
print(f"Newest product: {newest_product.name}, Manufacture Date: {newest_product.manufacture_date}")
