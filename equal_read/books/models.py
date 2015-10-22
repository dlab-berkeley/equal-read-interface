from django.db import models


# class reviewers(models.Model):
#     listTitle = models.CharField(maxlength=1000)
#     title = models.CharField(maxlength=1000)
#     MALE = 'Male'
#     FEMALE = 'Female'
#     genderChoices = {
#         (MALE, 'Male'),
#         (FEMALE, 'Female'),
#         (OTHER, )
#     }
#     gender = models.CharField(max_length=10,
#         choices=genderChoices)
#     roles = 
#     ages = 
#     ethnicityCode =
#     abilityCode =
#     sexualOrientation =
#     education =
#     income =
#     religiousBeliefs =
#     geography =
#     familyStatus =
#     notes = models.CharField(maxlength = 20)
#     nationality =
#     authorCode = ('representative', 'not representative', 'unknown')
#     era = ('historic', 'contemparary', 'ambiguous')


class Book(models.Model):
    listTitle = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    source = models.CharField(max_length=1000) 
    isbn = models.BigIntegerField(default=0)
    author = models.CharField(max_length=1000)
    illustrator = models.CharField(max_length=1000)
    publisher = models.CharField(max_length=1000)
    year = models.DateField()
    pages = models.PositiveIntegerField()
    readingLevel = models.CharField(max_length=1000)
    gradeLevel = models.CharField(max_length=1000)
    nameOfReader = models.CharField(max_length=1000)
    gender = models.CharField(max_length=1000)
    genderExpression = models.CharField(max_length=1000)
    age = models.PositiveSmallIntegerField(default=0)
    ethnicity = models.CharField(max_length=1000)
    disability = models.CharField(max_length=1000)
    sexualOrientation = models.CharField(max_length=1000)
    education = models.CharField(max_length=1000)
    income = models.CharField(max_length=1000)
    religion = models.CharField(max_length=1000)
    geography = models.CharField(max_length=1000)
    familyStatus = models.CharField(max_length=1000)
    notesByReader = models.CharField(max_length=1000)

    # import @python_2_unicode_compatible if desired
    def __str__(self):
        return self.title
