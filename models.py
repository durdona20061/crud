from django.db import models

gender = ('man', 'woman')


class Movie(models.Model):
    name = models.CharField(max_length=150)
    year = models.IntegerField()
    imdb = models.ImageField(upload_to='photos/%Y/%m/%d/',null=True,blank=True)
    genre = models.CharField(max_length=50, )
    actor = models.ManyToManyField('Actor')

    def __str__(self):
        return self.name


class Actor(models.Model):
    gender = (
        ('m', 'man'),
        ('w', 'woman'),
    )

    name = models.CharField(max_length=150)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10, choices=gender, default='man')

    def __str__(self):
        return self.name