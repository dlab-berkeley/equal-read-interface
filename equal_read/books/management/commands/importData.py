from django.core.management.base import BaseCommand, CommandError
from books.models import Book

import csv


class Command(BaseCommand):
    help = 'Import sample data for testing purpose'

    def add_arguments(self, parser):
        parser.add_argument('import')

    def handle(self, *args, **options):
        with open('books/sampleData.csv', 'rt') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                for i in range(32):
                    if row[i] == '':
                        row[i] = None
                bookObject = Book(listTitle=row[0], title=row[3], source=row[1], isbn=row[2], author=row[4], illustrator=row[5],
                    publisher=row[6], year=row[7], pages=row[8], readingLevel=row[9], gradeLevel=row[10], nameOfReader=row[11], gender=row[12],
                    genderExpression=row[13], age=row[14], ethnicity=row[15], disability=row[16], sexualOrientation=row[17], education=row[18], income=row[19],
                    religion=row[20], geography=row[21], familyStatus=row[22], notesByReader=row[23])
                bookObject.save()
