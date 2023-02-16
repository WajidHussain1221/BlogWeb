from django.db import models



class Subject(models.Model):
    subject_code = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=200)
    subject_description = models.TextField()

    def __str__(self):
        return self.subject_name

class Paper(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=200)
    source_file = models.FileField()

    def __str__(self):
        return  self.display_name