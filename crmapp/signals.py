from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Customer

# signals are created to perform any task behind simultaneously with other task
# in this, one is sender, other is receiver, we have to connect signal with right receiver
# using either .connect method or decorator

# receiver function
def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,
        )
        #print('Profile created!')

# connecting signals to receiver
post_save.connect(customer_profile, sender=User)
