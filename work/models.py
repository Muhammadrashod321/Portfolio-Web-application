from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=221)
    created_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Work(models.Model):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to="work/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    url = models.CharField(max_length=221)
    views = models.PositiveBigIntegerField()
    created_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title