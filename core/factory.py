from factory.django import DjangoModelFactory

class UserFactory(DjangoModelFactory):

    class Meta:

        model = 'core.User'
        django_get_or_create = ('username', 
                                'email', 
                                'password')


    username = 'Arthur'
    email = 'arthur0139@gmail.com'
    password = '123'

