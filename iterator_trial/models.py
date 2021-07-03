from django.db import models

# for Django tutorial
class Category(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name

# for Django tutorial
class SubCategory(models.Model):
    class Gender(models.IntegerChoices):
        ALL = 0
        MEN = 1
        WOMEN = 2

    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    gender = models.IntegerField(max_length=11, default=0, choices=Gender.choices)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name