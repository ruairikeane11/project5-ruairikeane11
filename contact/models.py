from django.db import models


# Create your models here.
class Contact(models.Model):
    """
    Stores a single contact form request related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} | {self.created_on}"
