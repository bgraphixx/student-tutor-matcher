from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Students(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    AGE = (
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
    )
    PARENTAL_STATUS = (
        ('Togther', 'Together'),
        ('Apart', 'Apart'),
    )
    GUARDIAN = (
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Other', 'Other'),
    )
    INTENTION = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    ROMANTIC = (
       ('Yes', 'Yes'),
        ('No', 'No'),
    )
    EXTRA = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    ALCOHOL = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    FAILURES = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
    )
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    student_id = models.IntegerField()
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    parental_status = models.CharField(max_length=200)
    guardian = models.CharField(max_length=200)
    intention = models.CharField(max_length=200)
    romantic = models.CharField(max_length=200)
    extra_curr = models.CharField(max_length=200)
    alcohol_cons = models.CharField(max_length=200)
    no_of_failures = models.CharField(max_length=200)
    grade1 = models.IntegerField()
    grade2 = models.IntegerField()
    grade3 = models.IntegerField()
    result = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

    class Meta:
        verbose_name_plural = "Students"


class Pass(models.Model):
    STYLE = (
        ('Visual', 'Visual'),
        ('Auditory', 'Auditory'),
        ('Kinesthetic', 'Kinesthetic'),
    )
    PERSONALITY = (
        ('Introvert', 'Introvert'),
        ('Extrovert', 'Extrovert'),
        ('Feeling', 'Feeling'),
        ('Intuitive', 'Intuitive'),
    )
    SUBJECTS = (
        ('Mathematics', 'Mathematics'),
        ('English', 'English'),
        ('Physics', 'Physics'),
    )
    student = models.ForeignKey(Students, on_delete=models.CASCADE, null=False)
    learning_styles = models.CharField(max_length=200, default=None)
    personality_styles = models.CharField(max_length=200, default=None)
    area_of_interests = models.CharField(max_length=200, default=None)

    class Meta:
        verbose_name_plural = "Pass"

    def __str__(self):
        return str(self.student)

class Fail(models.Model):
    STYLE = (
    ('Visual', 'Visual'),
    ('Auditory', 'Auditory'),
    ('Kinesthetic', 'Kinesthetic'),
    )
    PERSONALITY = (
    ('Introvert', 'Introvert'),
    ('Extrovert', 'Extrovert'),
    ('Feeling', 'Feeling'),
    ('Intuitive', 'Intuitive'),
    )
    SUBJECTS = (
    ('Mathematics', 'Mathematics'),
    ('English', 'English'),
    ('Physics', 'Physics'),
    )
    student = models.ForeignKey(Students, on_delete=models.CASCADE, null=False)
    learning_styles = models.CharField(max_length=200, default=None)
    personality_styles = models.CharField(max_length=200, default=None)
    area_of_interests = models.CharField(max_length=200, default=None)
    

    class Meta:
        verbose_name_plural = "Fail"

    def __str__(self):
        return str(self.student)

class Match(models.Model):
    student = models.ForeignKey(Fail, on_delete=models.CASCADE, null=False)
    tutor = models.ForeignKey(Pass, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = "Match"

    def __str__(self):
        return str(self.student) + " is tutored by " + str(self.tutor)