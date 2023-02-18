from django.db import models

# Create your models here.
class Semester(models.Model):
    table = models.CharField(max_length=200)                                # 시간표 이름
    credits = models.IntegerField(default=0)                                         # 이수 단위
    grade = models.FloatField(default=0.00)                                             # 학점 평점
    create_at = models.DateTimeField()                                      # create 시간
    update_at = models.DateTimeField(null=True, blank=True)                 # update 시간
    
    
    def __str__(self):
        return self.table

class Subjects(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)        # 과목에 연결할 semester model
    name = models.CharField(max_length=200)                                 # 과목 이름
    credit = models.IntegerField(default=0)                                          # 과목의 이수 인정 학점
    create_at = models.DateTimeField()                                      # create 시간
    update_at = models.DateTimeField(null=True, blank=True)                 # update 시간