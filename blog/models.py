from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=100)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text="One word for title alias.")
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text')
    content = models.TextField('CONTENT')
    created_at = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modified_at = models.DateTimeField('MODIFY DATE', auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-modified_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail')
    
    def get_previous(self):
        return self.get_previous_by_modified_at()
    
    def get_next(self):
        return self.get_next_by_modified_at()
# Create your models here.
