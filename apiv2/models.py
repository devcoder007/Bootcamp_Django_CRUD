from django.db import models
import uuid

# Create your models here.
class UsersAPI(models.Model):
    name = models.CharField(unique=False, max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(unique=False, max_length=50)



    def __str__(self):
        return self.email


class DisplayPhoto(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    image = models.FileField()


    def __str__(self):
        return self.title 