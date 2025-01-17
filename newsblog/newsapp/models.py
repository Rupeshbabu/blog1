from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "blogs"

    def __str__(self):
        return f'{self.title}'
