from django.db import models

# Create your models here.
class Post(models.Models):
    Title = models.Charfield(max_length=200)
    slug = models.Slugfield(unique=True, max_length=255)
    Text = models.TextFiled()
    author = get_user_model 
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)