from mongoengine import *

class Products(Document):
    title = StringField(max_length=255)
    description = StringField(max_length=2048)
    price = DecimalField(min_value=0)

class User(Document):
    fullname = StringField(max_length=255,min_length=3)
    login = StringField(max_length=30, min_length=8)
    password = StringField(min_length=8, required=True)
    bill = DecimalField(min_value=0)
    number = IntField()
    wishes = ListField(ReferenceField(Products))


    def __str__(self):
        return self.fullname

    def get_users_wishers(self):
        return self.wishes


if __name__ == "__main__":
    connect('db_example')
    # prodact_obj = Products(title='Iphone11', description='This is phone', price=20000).save()
    # prodact_obj1 = Products(title='BMW x5', description='This is car', price=1000000).save()
    # user = User(
    #     fullname = 'HigeLilu',
    #     login = 'lilulase',
    #     password='lilulase',
    #     bill=10500.50,
    #     number=125,
    #     wishes = [prodact_obj, prodact_obj1]
    # )
    # user.save()

    new_product = Products.objects.create(
        title='Mackboock',
        price=30000
    )
    user = User.objects.get(fullname='HigeLilu')
    user.wishes.append(
        new_product
    )
    print(user.wishes)
    products = Products.objects(price__gte=30000)
    print(products.to_json())