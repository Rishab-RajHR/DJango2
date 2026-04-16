class Student(models.Model):
    name = models.CharField()
    age = models.IntegerField()
    
    Student = Student.objects.all()