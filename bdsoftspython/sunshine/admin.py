from django.contrib import admin
from .models import Student, Contact


# Register your models here.
class Student_Admin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'phone']

    class Meta:
        model = Student
        admin.site.register(Student)


class Contact_Admin(admin.ModelAdmin):
    list_display = ['email', 'subject', 'message']

    class Meta:
        models = Contact
        admin.site.register(Contact)
