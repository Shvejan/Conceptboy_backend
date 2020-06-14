from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()

    class Meta:
        ordering = ['created']

    def __str__(self):
         return self.title



class Subject(models.Model):
   name = models.CharField(max_length = 50)
   def __str__(self):
       return self.name


class Category(models.Model):
   name = models.CharField(max_length = 50)
   subject = models.ForeignKey('Subject',on_delete=models.CASCADE,)
   def __str__(self):
        return self.name

class Subcategory(models.Model):
   name = models.CharField(max_length = 50)
   category = models.ForeignKey('Category',on_delete=models.CASCADE,)
   def __str__(self):
       return self.name

class Video(models.Model):
    name = models.CharField(max_length = 50)
    video_url=models.URLField()
    category = models.ForeignKey('Category',on_delete=models.CASCADE,)
    subcategory = models.ForeignKey('Subcategory',on_delete=models.CASCADE,)

    def __str__(self):
        return self.name
