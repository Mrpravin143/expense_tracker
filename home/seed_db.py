from faker import Faker
from home.models import *
import random
fake = Faker('en_IN')


def SeedDB(records=10)->None:
    allcollege = Colleges.objects.all()
    
 
    for i in range(records):
        student_name=fake.name()
        age=random.randint(18,30)
        gender=random.choice(['Male','Female'])
        email=fake.email()
        phone_number=fake.phone_number()
        randoms=random.randint(1,records)
        college=random.choice(allcollege)

        StudentData.objects.create(
            student_name=student_name,
            age=age,
            gender=gender,
            email=email,
            phone_number=phone_number,
            colleges_name=college
       
           

        )




def AuthorFake(records=100)->None:
    authors = Author.objects.all()

    for i in range(records):
        book_name=fake.name()
        book_price=random.randint(50,600)
        published_date=fake.date()
        total_sales=random.randint(1,20)
        author=random.choice(authors)

        Books.objects.create(
            book_name=book_name,
            book_price=book_price,
            published_date=published_date,
            total_sales=total_sales,
            author=author
            )





  

    



    


        



