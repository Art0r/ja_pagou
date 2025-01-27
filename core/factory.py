from factory.django import DjangoModelFactory
from factory import LazyAttribute
from faker import Faker
from core.models import User
import random


faker: Faker = Faker()
class UserFactory(DjangoModelFactory):

    def __init__(self) -> None:
        super().__init__()

    class Meta:

        model = 'core.User'
        django_get_or_create = ('username', 
                                'email', 
                                'password',
                                'first_name',
                                'last_name')

    username = LazyAttribute(lambda _: faker.user_name())
    email = LazyAttribute(lambda _: faker.email())
    password = LazyAttribute(lambda _: faker.password())
    first_name = LazyAttribute(lambda _: faker.first_name())
    last_name = LazyAttribute(lambda _: faker.last_name())


class PaymentFactory(DjangoModelFactory):

    def __init__(self) -> None:
        super().__init__()


    class Meta:

        model = 'core.Payment'
        django_get_or_create = ('receiver', 
                                'payier', 
                                'value')

    receiver = LazyAttribute(lambda _: random.choice(User.objects.all()))
    payier = LazyAttribute(lambda _: random.choice(User.objects.all()))
    value = LazyAttribute(lambda _: random.randint(0, 1000))
