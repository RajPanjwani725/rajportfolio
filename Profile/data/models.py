from django.db import models
from datetime import date
# Create your models here.

class Project(models.Model):
    your_choices = (
        ('Yes', 'Yes'),
        ('No','No'),

    )



    project_name=models.CharField(max_length=500)
    project_description=models.TextField(max_length=1000)
    project_technologies=models.TextField(max_length=500)
    project_upload_to_youtube=models.CharField(max_length=100,choices=your_choices,default="")
    project_link_youtube = models.TextField(max_length=500,blank=True)
    project_link_linkedin = models.TextField(max_length=500,default="",blank=True)
    project_link_github = models.TextField(max_length=500, default="")
    project_live_link=models.TextField(max_length=500,default="",blank=True)
    project_image = models.ImageField(upload_to="static/assets/uploads", default="",blank=True)

    project_tools=models.CharField(max_length=500,default='')

    def __str__(self):
        return self.project_name
class Certification(models.Model):
    certification_name=models.CharField(max_length=100)
    certification_publication=models.CharField(max_length=500)
    certification_date=models.DateField(default=None)
    certification_link=models.TextField(default="")

    def __str__(self):
        return self.certification_name


class Education(models.Model):
    education_college=models.CharField(max_length=500)
    education_course = models.CharField(max_length=500,default="")
    education_description = models.TextField(max_length=5000,default="")
    education_degree=models.CharField(max_length=500)
    education_gpa=models.CharField(max_length=10)
    education_start=models.IntegerField()
    education_end=models.IntegerField()
    def __str__(self):
        return self.education_college

class Company(models.Model):
    company_name=models.CharField(max_length=500,default="")
    company_role = models.CharField(max_length=500, default="")
    company_start_date=models.DateField(default=None)
    company_end_date=models.DateField(default=None,blank=True)
    company_role_description=models.TextField(max_length=5000,default="")
    company_role_logo = models.ImageField(upload_to="static/assets/uploads", default="", blank=True)

    def __str__(self):
        return self.company_name
