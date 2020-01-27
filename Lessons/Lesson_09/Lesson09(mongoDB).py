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

if __name__ == "__main__":
    connect('db_example')
    user = User.objects.create(
        fullname = 'Lilu',
        login = 'lilulase',
        password='lilulase',
        bill=10500.50,
        number=124
    )
    # print(user.fullname,user.login,user.password,user.number,user.bill)

    # users = User.objects(fullname='Rumba')
    #
    # for user in users:
    #     print(user)