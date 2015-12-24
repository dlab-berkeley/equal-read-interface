from django.core.management.base import BaseCommand, CommandError
from books.models import Book

import csv, random, datetime


class Command(BaseCommand):
    help = 'Import sample data for testing purpose'

    def add_arguments(self, parser):
        parser.add_argument('filepath')

    def handle(self, *args, **options):
        # self.stdout.write(options['filepath'])
        with open(options['filepath'], 'rt') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                bookObject = Book(listTitle=row[0], title=row[3], source=row[1], isbn=row[2], author=row[4], illustrator=row[5],
                    publisher=row[6], year=2015, pages=0, readingLevel=row[9], gradeLevel=row[10], nameOfReader=row[11], gender=row[12],
                    genderExpression=row[13], age=0, ethnicity=row[15], disability=row[16], sexualOrientation=row[17], education=row[18], income=0,
                    religion=row[20], geography=row[21], familyStatus=row[22], notesByReader=row[23])
                bookObject.save()
