from demo.models import Parents,Childs
from faker import Faker
import random


fake = Faker()


def DummyDate(Records = 10):
    for data in Records:
        name = fake.name()
        mobile = random.randint(0000000000,9999999999)
        gender = random.choice(['Male','Female'])
        age = random.randint(18,29)

        Parents.objects.create(
            name=name,
            mobile=mobile,
            gender=gender,
            age=age
        )

    print("✅ Data Load Success !")


DummyDate(100)
