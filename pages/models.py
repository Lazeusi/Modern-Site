from django.db import models

# Create your models here.

class SlideImges(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        if self.title:
            return self.title
        return str(self.image)