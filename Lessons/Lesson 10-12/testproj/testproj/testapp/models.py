from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(blank=False, primary_key=True)
    test = models.CharField(blank=False, max_length=100, default='test')

    def __str__(self):
        return self.email

class Post(models.Model):
    POST_TYPES = [('C', 'Copyright'), ('P', 'Public License'), ('A', 'Commercial')]

    title = models.CharField(blank=False, max_length=100)
    subtitle = models.CharField(max_length=200)
    content = models.TextField(blank=False)
    issued = models.DateTimeField()
    post_type = models.CharField(blank=False, max_length=1, choices=POST_TYPES)
    image = models.ImageField(upload_to='uploads')

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
