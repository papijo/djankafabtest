from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse




class Tag(models.Model):
    name = models.CharField(max_length = 150, db_index = True)
    slug = models.SlugField(max_length = 150, db_index = True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    

    class Meta:
        ordering = ('name', )
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('blog:post_list_by_tag', args=[self.slug])






class Post(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200, null = True)
    tag = models.ForeignKey(Tag, related_name='posts', on_delete = models.CASCADE, null = True)
    summary = models.CharField(max_length = 200, null = True)
    text= models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date= models.DateTimeField(blank = True, null = True)
    image = models.ImageField(upload_to='blog/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title

    def get_tag_list(self):
        return (self.tag)

    class Meta:
        ordering = ["-published_date"]
