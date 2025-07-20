from demo.models import Parents,Childs
from faker import Faker
import random


fake = Faker()


def DummyDate(Records):
    ids = Parents.objects.all()
    for data in range(Records):
        name = fake.name()
        mobile = random.randint(0000000000,9999999999)
        gender = random.choice(['Male','Female'])
        age = random.randint(18,29)
        parent = ids.id()

        Parents.objects.create(
            name=name,
            mobile=mobile,
            gender=gender,
            age=age
        )

    

    print("✅ Data Load Success !")


# DummyDate()


def ChildData(Records):
    for data in range(Records):
        name_of_chlid = fake.name()
        age_of_child = random.randint(18,30)
        branch = random.choice(['BCA','BBA','BMS','BA','B.com','Pharmachy','B.sc'])

        Childs.objects.create(
            name_of_chlid=name_of_chlid,
            age_of_child=age_of_child,
            branch=branch
        )

    print("✅ Data Loaded Suceess ....")

ChildData(100)


    
