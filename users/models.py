from django.db import models

class User(models.Model):
    user = models.OneToOneField("auth.User",on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password=models.CharField(max_length=225)

    class Meta:
        db_table = "users"
        
    def __str__(self):
        return self.username
