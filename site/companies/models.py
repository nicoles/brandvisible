from django.db import models

# Create your models here.
class Company (models.Model):
    name = models.CharField(max_length=255)
    cik = models.IntegerField()
    parent = models.ManyToManyField("self")
    top_parent = models.ManyToManyField("self")
    top_parent_of = models.ManyToManyField("self")

    def __unicode__(self):
        return self.name

class Lookup (models.Model):
    company = models.ForeignKey(Company)
    date = models.DateTimeField('lookup date')

    def __unicode__(self):
        return self.company

class Aliases (models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
