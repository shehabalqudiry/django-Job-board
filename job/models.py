from django.db import models

# Create your models here.


class Job(models.Model):
    objects = None
    JOB_TYPE = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    )
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 
