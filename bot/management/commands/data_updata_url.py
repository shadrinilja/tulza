import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tulza.settings")
django.setup()
from django.core.management.base import BaseCommand
from bot.models import Bb
from bot.models import Inquiry
import logging
from urllib.parse import urlsplit, urlencode
import json
from urllib.request import urlopen
import time
from urllib.error import URLError

start_time = time.time()

take_default_json = Inquiry('https://bus.gov.ru/public/agency/agency_tasks.json?agency=182691&task=')
take_default_address = take_default_json.get_start_url()
prs_default_dict = take_default_json.InquiryPrs()

__const_url = 'https://bus.gov.ru/public/download/download.html?id='

prs_download_doc = Inquiry(__const_url)
get_get_prs_inquiry_doc = prs_download_doc.get_start_url()
prs_part_doc = prs_download_doc.InquiryPrs()

class JsonParse:
    def __init__(self,inquiry):
        self.inquiry = inquiry
    def AssemblyInquiry(self):##Собираем запрос
        tro = urlsplit(self.inquiry).scheme+'://'+ urlsplit(self.inquiry).netloc \
              + urlsplit(self.inquiry).path +'?'+urlencode(prs_default_dict)
        return tro
    def AssemblyInquiry_2(self):##Собираем запрос
        tro = urlsplit(self.inquiry).scheme+'://'+ urlsplit(self.inquiry).netloc \
              + urlsplit(self.inquiry).path +'?'+urlencode(prs_part_doc)
        return tro
class Command(BaseCommand):
    def handle(self, *args, **options):
        for tro in Bb.objects.all():
            try:
                a = []
                lo = str(tro.id_ogr)
                old_pk = tro.pk
                itreete_old_pk = Bb.objects.get(pk=old_pk)
                old_url = itreete_old_pk.url_pars
                prs_default_dict['agency'] = lo
                prs_default_dict['task'] = ''
                a = JsonParse(take_default_address).AssemblyInquiry()
                response = urlopen(a)
                data_json = json.loads(response.read())
                tasks_dict = data_json['tasks']
                task = tasks_dict[-1:]
                for last_year in task:
                    for key, values in last_year.items():
                        all_last_year = last_year.get('id')
                Prs_tasks = prs_default_dict
                Prs_tasks['task'] = all_last_year
                b = JsonParse(take_default_address).AssemblyInquiry()
                print(b)
                response = urlopen(b)
                data_json = json.loads(response.read())
                pubDate = data_json['currentTask']['attachments'][0]['publishDate']  ## Актуальная дата
                print(pubDate)
                name_title = tro.name
                new_tittle_name = name_title.split()
                del new_tittle_name[0:4]
                string_titile_name = ' '.join(new_tittle_name)
                doc = data_json['currentTask']['attachments'][0]['id']  ##Докумаент
                print(doc)
                old_url_doc = itreete_old_pk.url_doc
                inn = tro.inn
                print(inn)
                InquiryParse = prs_part_doc
                InquiryParse['id'] = doc
                c = JsonParse(get_get_prs_inquiry_doc).AssemblyInquiry_2()
                print(c)
                obj_url_doc = Bb.objects.get(id=tro.pk)
                obj_url_doc.url_doc = c
                obj_url_doc.save()
            except TimeoutError:
                pass
            except URLError:
                pass
        print('1:' + str(start_time - time.time()))