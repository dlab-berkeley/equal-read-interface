from django.db import models

# TODO Needs to be completed
# class reviewers(models.Model):
#     title = models.CharField(maxlength = 20)
#     gender = ('M', 'F', 'All')
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


class book(models.Model):
    title = models.CharField(max_length=1000)
