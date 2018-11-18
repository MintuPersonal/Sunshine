from django.db import models


# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
        # return [self.first_name, self.last_name, self.phone]


class Contact(models.Model):
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=196)
    message = models.TextField()

    def __str__(self):
        return self.email
        # return [self.email, self.subject, self.message]
