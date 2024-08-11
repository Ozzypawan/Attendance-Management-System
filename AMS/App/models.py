from django.db import models

# Create your models here.

class UserAuth(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_email = models.EmailField(default=None)

    def __str__(self):
        return self.user_name