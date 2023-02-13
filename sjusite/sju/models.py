from django.db import models

# Create your models here.
class Semester(models.Model):
    table = models.CharField(max_length=200)    # 시간표 이름
    credit = models.IntegerField()              # 이수 단위
    grade = models.FloatField()                 # 학점 평점
    create_at = models.DateTimeField()
    def __str__(self):
        return self.table

class Subjects(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField()