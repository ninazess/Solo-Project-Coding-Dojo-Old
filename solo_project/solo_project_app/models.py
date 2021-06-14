
from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        
        if not EMAIL_REGEX.match(postData['email']):         
            errors['email'] = ("Invalid email address!")

        email_check = User.objects.filter(email=postData['email'])
        if email_check:
            errors['duplicate'] = "Email Address already exists"

        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"

        if postData['password'] != postData['confirm_password']:
            errors['password'] = "Passwords do not match"

        return errors

    def register(self, postData):
        pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()

        return User.objects.create(
            first_name = postData['first_name'],
            last_name = postData['last_name'],
            email = postData['email'],
            address = postData['address'],
            password = pw,
        )

    def authenticate(self, email, password):
        users=User.objects.filter(email=email)
        if users:
            user=users[0]
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                return True
            else:
                return False
        return False

class Address(models.Model):
    street = models.TextField()
    city = models.TextField()
    state = models.TextField()
    code = models.TextField()

class User(models.Model):
    first_name = models.CharField(max_length=55, blank = False, null = False)
    last_name = models.CharField(max_length=55, blank = False, null = False)
    email = models.EmailField(unique=True)
    address = models.ForeignKey(Address, related_name="users", on_delete = models.CASCADE)
    liquor = models.CharField(max_length=55)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()



# class Subscription(models.Model):
    