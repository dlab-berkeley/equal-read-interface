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
    listTitle = models.CharField(maxlength=1000)
    title = models.CharField(max_length=1000)
    source = 
    isbn = 
    author = 
    illustrator = 
    publisher = 
    year = 
    pages = 
    readingLevel = 
    gradeLevel = 
    nameOfReader = 
    gender = 
    genderExpression = 
    age = 
    ethnicity = 
    disability = 
    sexualOrientation = 
    education = 
    income = 
    religion = 
    geography = 
    familyStatus = 
    notesByReader = 

    # import @python_2_unicode_compatible if desired
    def __str__(self):
        return self.title
