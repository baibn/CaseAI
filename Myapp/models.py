from django.db import models


# Create your models here.

class DB_News(models.Model):
    content = models.TextField()
    ctime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]

class DB_projects(models.Model):
    name = models.CharField(max_length=30,default='')
    src_case_set= models.TextField(default=[])
    old_srs = models.TextField(default='')
    def __str__(self):
        return self.name

class DB_new_srs(models.Model):
    content = models.TextField(null=True)
    project_id = models.IntegerField(default=0)
    def __str__(self):
        return str(self.project_id)