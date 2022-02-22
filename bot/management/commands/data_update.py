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

logger = logging.getLogger('trololo')

start_time = time.time()
__const_url = 'https://bus.gov.ru/public/download/download.html?id='

prs_download_doc = Inquiry(__const_url)
get_get_prs_inquiry_doc = prs_download_doc.get_start_url()
prs_part_doc = prs_download_doc.InquiryPrs()



class JsonParse:
    def __init__(self, inquiry):
        self.inquiry = inquiry
    def AssemblyInquiry(self):##Собираем запрос
        tro = urlsplit(self.inquiry).scheme+'://'+ urlsplit(self.inquiry).netloc \
              + urlsplit(self.inquiry).path +'?'+urlencode(prs_part_doc)

class Command(BaseCommand):
    def handle(self, *args, **options):
        for tro in Bb.objects.all():
            forlink = tro.url_pars
            response = urlopen(forlink)
            data_json = json.loads(response.read())
            pubDate = data_json['currentTask']['attachments'][0]['publishDate']## Актуальная дата
            doc = data_json['currentTask']['attachments'][0]['id'] ##Докумаент
            tm = tro.pk
            lool = Bb.objects.get(pk=tm)
            pepe = lool.publishDate ## Дата из бд
            current_document_now = lool.url_doc
            current_update_status = lool.update_status

            if pepe < pubDate or pepe > pubDate:
                new_time = Bb.objects.filter(publishDate=pepe).update(publishDate=pubDate)
                InquiryParse = prs_part_doc
                InquiryParse['id'] = doc
                c = JsonParse(get_get_prs_inquiry_doc).AssemblyInquiry()
                new_obj_url_doc = Bb.objects.filter(url_doc=current_document_now).update(url_doc=c)
                new_update_status = Bb.objects.filter(update_status=current_update_status).update(
                    update_status='обновилось')
                logger.info('обновилось')
            else:
                not_new_update_status = Bb.objects.filter(update_status=current_update_status).update(
                    update_status='не обновилось')
                logger.info('не обновилось')

        print('1:'+str(start_time-time.time()))

