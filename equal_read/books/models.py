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
    listTitle = models.CharField(max_length=1000, null=True)
    title = models.CharField(max_length=1000, null=True)
    source = models.CharField(max_length=1000, null=True) 
    isbn = models.CharField(max_length=13, null=True)
    author = models.CharField(max_length=1000, null=True)
    illustrator = models.CharField(max_length=1000, null=True)
    publisher = models.CharField(max_length=1000, null=True)
    year = models.CharField(max_length=4, null=True)
    pages = models.CharField(max_length=1000, null=True)
    readingLevel = models.CharField(max_length=1000, null=True)
    gradeLevel = models.CharField(max_length=1000, null=True)
    nameOfReader = models.CharField(max_length=1000, null=True)
    gender = models.CharField(max_length=1000, null=True)
    genderExpression = models.CharField(max_length=1000, null=True)
    age = models.CharField(max_length=1000, null=True)
    ethnicity = models.CharField(max_length=1000, null=True)
    disability = models.CharField(max_length=1000, null=True)
    sexualOrientation = models.CharField(max_length=1000, null=True)
    education = models.CharField(max_length=1000, null=True)
    income = models.CharField(max_length=1000, null=True)
    religion = models.CharField(max_length=1000, null=True)
    geography = models.CharField(max_length=1000, null=True)
    familyStatus = models.CharField(max_length=1000, null=True)
    notesByReader = models.CharField(max_length=1000, null=True)

    # import @python_2_unicode_compatible if desired
    def __str__(self):
        return self.title
