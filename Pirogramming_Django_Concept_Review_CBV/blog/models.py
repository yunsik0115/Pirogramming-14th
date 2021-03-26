from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=100)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text="One word for title alias.")
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text')
    content = models.TextField('CONTENT')
    created_at = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modified_at = models.DateTimeField('MODIFY DATE', auto_now=True)
    tags = TaggableManager(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="OWNER", blank=True, null=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-modified_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))
    
    def get_previous(self):
        return self.get_previous_by_modified_at()
    
    def get_next(self):
        return self.get_next_by_modified_at()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
# Create your models here.
