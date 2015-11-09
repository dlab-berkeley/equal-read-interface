from django.core.management.base import BaseCommand, CommandError
from books.models import Book

import csv
import random


class Command(BaseCommand):
    help = 'Import sample data for testing purpose'

    def add_arguments(self, parser):
        parser.add_argument('import')

    def handle(self, *args, **options):
        authors = ['Yiyang', 'Yadel', 'Susan', 'Dav']
        genders = ['male', 'female']
        with open('books/sampleData.csv', 'rt') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row[0] == '':
                    row[0] = row[3]
                if row[1] == '':
                    row[1] = 'dlab'
                if row[2] == '':
                    row[2] = random.choice(range(1e13, 1e14))
                if row[4] == '':
                    row[4] = random.choice(authors)
                if row[5] == '':
                    row[5] = random.choice(authors)
                if row[6] == '':
                    row[6] = 'dlab'
                if row[7] == '':
                    row[7] = random.choice(range(2015))
                if row[8] == '':
                    row[8] = random.choice(range(100))
                if row[9] == '':
                    row[9] = 'unknown'
                if row[10] == '':
                    row[10] = 'unknown'
                if row[11] == '':
                    row[11] = random.choice(authors)
                if row[12] == '':
                    row[12] = random.choice(genders)
                if row[13] == '':
                    row[13] = ''
                if row[14] == '':
                    row[14] = random.choice(range(120))
                if row[15] == '':
                    row[15] = 'not specified'
                if row[16] == '':
                    row[16] = 'None'
                if row[17] == '':
                    row[17] = 'unknown'
                if row[18] == '':
                    row[18] = 'Bachelor'
                if row[19] == '':
                    row[19] = random.choice(range(1e5))
                if row[20] == '':
                    row[20] = 'unknown'
                if row[21] == '':
                    row[21] = 'United States'
                if row[22] == '':
                    row[22] = 'Good'
                if row[23] == '':
                    row[23] = 'None'
                bookObject = Book(listTitle=row[0], title=row[3], source=row[1], isbn=row[2], author=row[4], illustrator=row[5],
                    publisher=row[6], year=row[7], pages=row[8], readingLevel=row[9], gradeLevel=row[10], nameOfReader=row[11], gender=row[12],
                    genderExpression=row[13], age=row[14], ethnicity=row[15], disability=row[16], sexualOrientation=row[17], education=row[18], income=row[19],
                    religion=row[20], geography=row[21], familyStatus=row[22], notesByReader=row[23])
                bookObject.save()
