from django.db import models

# Create your models here.

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Don't create table in DB


class Category(TimeStampModel):
     name = models.CharField(max_length=100)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     
class Tag(TimeStampModel):
     name = models.CharField(max_length=30)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

class Post(TimeStampModel):
     STATUS_CHOICES = [
          ('draft', 'Draft'),
          ('published','Published')
          
     ]
     title = models.CharField(max_length=255)
     content = models.TextField()
     feature_image = models.ImageField(upload_to="post_images/%y/%m/%d", blank=False)
     author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="published")
     view_count = models.PositiveBigIntegerField(default=0)
     published_at = models.DateTimeField(null=True, blank=True)
     category = models.ForeignKey(Category, on_delete=models.CASCADE)
     tag = models.ManyToManyField(Tag)
     
     def __str__(self):
          return self.title
     