import datetime

from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title

    # class Meta:
    #     db_table = ''
    #     managed = True
    #     verbose_name = 'ModelName'
    #     verbose_name_plural = 'ModelNames')
