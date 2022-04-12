from django.db import models
import json
from urllib.request import urlopen
from urllib.error import HTTPError
import time
from urllib.parse import urlsplit, parse_qs, urlencode
start_time = time.time()


class Bb(models.Model):
    name = models.CharField(max_length=350, verbose_name='название')
    id_ogr = models.IntegerField(null=True, verbose_name='id организации')
    inn = models.BigIntegerField(null=True, verbose_name='инн организации')
    actual_year = models.IntegerField(null=True, verbose_name='актуальный год')##Task
    url_pars = models.URLField(null=True, max_length=200, verbose_name='урл_для парсинга')
    publishDate = models.BigIntegerField(null=True, verbose_name='время публикации')
    url_doc = models.URLField(max_length=200, null=True, verbose_name='Ссылка на актуальный документ')
    update_status = models.CharField(max_length=200, null=True, verbose_name='состояние обновления')

    objects = models.Manager()

class Inquiry:##Парсим запрос
    def __init__(self, start_url):
        self.start_url = start_url
    def get_start_url(self):
        return self.start_url
    def InquiryPrs(self):
        query = urlsplit(self.start_url).query
        params = parse_qs(query)
        for key, val in params.items():##Делаем словарь из части запроса
            if len(val) == 1:
                params[key] = val[0]
        return params

class JsonParse:
    def __init__(self, inquiry,input_urlencode):
        self.inquiry = inquiry
        self.input_urlencode = input_urlencode
    def get_urlencode_input(self):
        return urlencode(self.input_urlencode)

    def AssemblyInquiry(self):##Собираем запрос
        tro = urlsplit(self.inquiry).scheme+'://'+ urlsplit(self.inquiry).netloc \
              + urlsplit(self.inquiry).path + '?'+ self.get_urlencode_input()
        return tro

take_default_json = Inquiry('https://bus.gov.ru/public/agency/agency_tasks.json?agency=182691&task=')
take_default_address = take_default_json.get_start_url()
prs_default_dict = take_default_json.InquiryPrs()

