from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=120)
    body=models.TextField()
    date=models.DateTimeField()

    def __str__(self):
        return self.title



    # class Meta:
    #     db_table = ''
    #     managed = True
    #     verbose_name = 'ModelName'
    #     verbose_name_plural = 'ModelNames')