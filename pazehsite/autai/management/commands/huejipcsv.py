import csv
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction
from autai.models import Record


class Command(BaseCommand):

    @transaction.atomic
    def handle(self, *args, **options):
        mia = os.path.join(
            settings.BASE_DIR, 'autai',
            'csv', '潘金玉《巴宰族母語錄音2184句》數位化 - 2184句.csv')
        print(mia)
        with open(mia) as csvfile:
            reader = csv.DictReader(csvfile)
            for pit in reader:
                print(pit)
                if pit['編號'] and pit['Pazeh'] and pit['華語'] and pit['頁碼']:
                    Record.objects.create(
                        csvid=pit['編號'],
                        pazeh=pit['Pazeh'],
                        hua=pit['華語'],
                        pageid=pit['頁碼']
                    )
                else:
                    print('(Skip)')
