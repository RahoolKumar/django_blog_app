
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# In model, each class creates its table in database and each attributes is a field in the table.
# Here is Post is table and title, content, date_posted and author are its rows.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # ForeignKey here means a single author can have multiple posts but a post can have only one author.
    # It is an example of oneToMany relationship.

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    
    
