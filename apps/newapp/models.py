from django.db import models
import datetime
import re
import bcrypt
import datetime


class Validator(models.Manager):
     def basic_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First Name should be at least 2 characters,letters only"
        elif len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name should be at least 2 characters"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email']='Invalid email adress'
        hello=User.objects.filter(email=(postData['email']))
        if hello:
            errors['duplicate']='email already exist...please create a new one'
        elif not  PASSWORD_REGEX.match(postData['password']):
            errors['password']='Password must be greater than 8 characters!Password must contain at least one lowercase letter, one uppercase letter, and one digit'
        return errors

     def login_validator(self,postData):
        errors={}
        user = User.objects.filter(email=(postData['email']))	
        if len(user) == 0:
            errors['email']='There is no such email'
        elif bcrypt.checkpw((postData['password']).encode(),user[0].password.encode()):
            print('hello')
        else:
            errors['password']="Invalid password"
        return errors
    

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length =255)
    email = models.CharField(max_length=255)
    password=models.CharField(max_length = 255)
    friends=models.ManyToManyField('self',related_name='friended_by')
    birthday=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=255)
    objects=Validator()
class Message(models.Model):
    message = models.CharField(max_length = 255)
    sent_from =models.ForeignKey(User,related_name='user_from')
    sent_to = models.ForeignKey(User,related_name='user_sent')
    created_at=models.DateTimeField(auto_now_add=True)



