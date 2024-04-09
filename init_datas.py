import os
import random
import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()


from items.models import Item
from logisticians.models import Logistician
from packages.models import Package


def generate_data():
    Logistician.objects.all().delete()
    Package.objects.all().delete()
    Item.objects.all().delete()

    logisticiens = []
    for _ in range(5):
        logisticiens.append(Logistician.objects.create(
            last_name='Last Name' + str(_),
            first_name='First Name' + str(_),
            email='logistician{}@test.com'.format(_)
        ))

    for _ in range(10):
        package = Package.objects.create(
            code='COL' + str(_),
            weight=random.uniform(1, 20),
            delivery_date=timezone.now() + timezone.timedelta(days=random.randint(1, 30)),
            status=random.choice(['In Shipping', 'Pending Dropoff']),
            logistician=random.choice(logisticiens)
        )

        for __ in range(random.randint(1, 5)):
            Item.objects.create(
                label='Item' + str(__),
                quantity=random.randint(1, 10),
                package=package
            )

    print("Data generated !")


if __name__ == '__main__':
    generate_data()

