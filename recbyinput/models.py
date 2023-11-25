from django.db import models

# Create your models here.
# Create your models here.
#모든 모델들은 models.Model 상속

class RecNames(models.Model):
    name1=models.CharField(max_length=150)
    name2=models.CharField(max_length=150)
    name3=models.CharField(max_length=150)
    name4=models.CharField(max_length=150)
    name5=models.CharField(max_length=150)

    def __str__(self):
        return f"{self.id}-{self.name1}"