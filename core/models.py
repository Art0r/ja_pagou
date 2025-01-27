from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Base(models.Model):
    '''
    This is the class that will be extended from all other models
    '''

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    pass

    def __str__(self):
        return self.email


class Payment(Base):

    receiver = models.ForeignKey(name='receiver', related_name='receiver_payment', 
                                    to=User, on_delete=models.DO_NOTHING)

    payier = models.ForeignKey(name='payier', related_name='pauir_payment',
                                  to=User, on_delete=models.DO_NOTHING)
    
    value = models.FloatField(blank=False, null=False)
