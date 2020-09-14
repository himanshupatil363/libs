from django.db import models

class info(models.Model):
    name = models.CharField(max_length=200)
    m_no = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    class Meta:
        db_table="student"

