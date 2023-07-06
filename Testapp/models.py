from django.db import models

# Create your models here.


class Gym_Member(models.Model):
    member_id=models.IntegerField()
    Name=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    password=models.CharField(max_length=200)
    mobile=models.CharField(max_length=100)
    is_active=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.Name


class Auth(models.Model):
    user_name=models.CharField(max_length=30)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=8)
    

