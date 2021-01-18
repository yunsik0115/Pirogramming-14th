from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100, validators=[]) #길이 제한 있음, validators로 valid 기준
    desc = models.TextField(blank=True) # 길이 제한 없음
    price = models.PositiveIntegerField()
    is_published = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'<{self.pk}> {self.name}'