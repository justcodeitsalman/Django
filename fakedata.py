import os 
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstProject.settings')
django.setup()  

from Testapp.models import *
from faker import Faker
from random import randint

fake=Faker()

def populate(n):
    for i in range (n):
        mem_id=fake.random_number(5)
        mem_name=fake.name()
        auth_user_name=fake.first_name()
        auth_password=fake.password(length=8)
    #print("date",fake.date())
        mem_email=fake.email()
        mem_mob=fake.random_int(min=0,max=9999999999)
        mem_stat=fake.boolean()
        '''
        def phone_num():
            d1=randint(7,9)
            num=str(d1)
            for i in range (9):
                num=num+str(randint(0,9))
            return int(num)
        
        
        user_phone=phone_num()
        '''
        #print("role",fake.random_element(elements=('admin','gym_owner','trainer','gym_member')))
        #print("Address,",fake.address())
        #print("city",fake.city())
        record=Gym_Member.objects.get_or_create(member_id=mem_id,Name=mem_name,email=mem_email,mobile=mem_mob,is_active=mem_stat)
        record2=Auth.objects.get_or_create(user_name=auth_user_name,email=mem_email,password=auth_password)


populate(10)





