from django.db import models

# Create your models here.

# class Category(models.Model):
#     category = models.CharField(max_length=100, null=False)
    
#     def __str__(self):
#         return self.category
    
class Event(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, null=False)
    event_name = models.CharField(max_length=100, null=False)
    starting_date = models.DateField()
    ending_date = models.DateField()
    
    def __str__(self):
        return "%s %s" %(self.category, self.event_name)
    
class Score(models.Model):
    category = models.CharField(max_length=100, null=False)
    event_name = models.CharField(max_length=100, null=False)
    num_stars = models.IntegerField()